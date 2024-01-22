from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
from cloudinary.models import CloudinaryField
from django.core.exceptions import ValidationError
from PIL import Image
from io import BytesIO
import cloudinary

# Define CATEGORY_CHOICES outside of the BlogPost class
CATEGORY_CHOICES = [
    ('SK', 'Skate'),
    ('MU', 'Music'),
    ('HI', 'History'),
]

class SubCategory(models.Model):
    name = models.CharField(max_length=100)
    # Use CATEGORY_CHOICES directly here
    parent_category = models.CharField(max_length=2, choices=CATEGORY_CHOICES)

    def __str__(self):
        return f"{self.get_parent_category_display()}: {self.name}"


def validate_square_image(image_field):
    image = Image.open(image_field)
    if image.width != image.height:
        raise ValidationError("The image is not square. Please upload a square image.")
    
class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    subcategory = models.ForeignKey(SubCategory, on_delete=models.SET_NULL, null=True, blank=False)
    image = CloudinaryField('image', blank=True, null=True, validators=[validate_square_image])
    youtube_video_url = models.URLField(blank=True, null=True, help_text="URL of the YouTube video")
    uploaded_video = CloudinaryField('video', blank=True, null=True, help_text="Please upload a square video (e.g., 480x480, 640x640).")
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
                    {'width': 300, 'height': 300, 'crop': 'fill', 'gravity': 'face'}
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
