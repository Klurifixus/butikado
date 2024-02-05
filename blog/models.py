import re
from io import BytesIO

import cloudinary
import requests
from cloudinary.models import CloudinaryField
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.db import models
from django.utils.text import slugify
from PIL import Image

# Define CATEGORY_CHOICES outside of the BlogPost class
CATEGORY_CHOICES = [
    ("SK", "Skate"),
    ("MU", "Music"),
    ("HI", "History"),
]


class SubCategory(models.Model):
    name = models.CharField(max_length=100)
    # Use CATEGORY_CHOICES directly here
    parent_category = models.CharField(max_length=2, choices=CATEGORY_CHOICES)

    def __str__(self):
        return f"{self.get_parent_category_display()}: {self.name}"


def validate_youtube_url(value):
    pattern = r"^(https?://)?(www\.)?(youtube\.com|youtu\.be)/.+$"
    if not re.match(pattern, value):
        raise ValidationError("Invalid YouTube URL")


def validate_square_image(image_field):
    if image_field:
        # Check if the image is stored on Cloudinary
        if hasattr(image_field, "public_id"):
            # Fetch the image from Cloudinary as a BytesIO object
            image_url = cloudinary.CloudinaryImage(image_field.public_id).build_url(
                secure=True
            )
            # Add timeout parameter
            response = requests.get(image_url, timeout=10)
            image = Image.open(BytesIO(response.content))
        else:
            # If not on Cloudinary, open the image directly
            image = Image.open(image_field)

        width, height = image.size

        if width != height:
            raise ValidationError(
                "The image is not square. Please upload a square image."
            )


class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    subcategory = models.ForeignKey(
        SubCategory, on_delete=models.SET_NULL, null=True, blank=False
    )
    image = CloudinaryField(
        "image", blank=True, null=True, validators=[validate_square_image]
    )
    youtube_video_url = models.URLField(
        blank=True,
        null=True,
        help_text="URL of the YouTube video (optional)",
        validators=[validate_youtube_url],
    )
    uploaded_video = CloudinaryField(
        "video",
        blank=True,
        null=True,
        help_text="Please upload a square video (e.g., 480x480, 640x640).",
    )
    content = models.TextField(max_length=10000)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    published_date = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(unique=True, blank=True)
    likes = models.IntegerField(default=0)
    dislikes = models.IntegerField(default=0)

    def total_likes(self):
        return PostInteraction.objects.filter(post=self, liked=True).count()

    def total_dislikes(self):
        return PostInteraction.objects.filter(post=self, disliked=True).count()

    def get_image_url(self):
        if self.image:
            return cloudinary.CloudinaryImage(self.image.public_id).build_url(
                transformation=[
                    {"width": 300, "height": 300, "crop": "fill", "gravity": "face"}
                ]
            )
        return None

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(BlogPost, self).save(*args, **kwargs)

    def __str__(self):
        return self.title


class PostInteraction(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(BlogPost, on_delete=models.CASCADE)
    liked = models.BooleanField(default=False)
    disliked = models.BooleanField(default=False)
