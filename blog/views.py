from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from django.http import HttpResponseForbidden
from django.contrib.auth.decorators import login_required
from .forms import BlogPostForm
from .models import BlogPost, SubCategory, PostInteraction
from django.views.decorators.http import require_POST
import cloudinary.uploader
import logging
import re

@login_required
def add_blog_post(request):
    if not request.user.is_superuser:
        return HttpResponseForbidden("You are not authorized to add a blog post.")

    if request.method == 'POST':
        form = BlogPostForm(request.POST, request.FILES)
        def extract_video_id(url):
            pattern = r'(?:https?://)?(?:www\.)?youtu(?:be\.com/watch\?v=|\.be/)([\w-]+)(?:&\S*)?$'
    
            # Use re.search to find the video ID in the URL
            match = re.search(pattern, url)
    
            if match:
                video_id = match.group(1)
                return video_id
            else:
                return None

        if form.is_valid():
            blog_post = form.save(commit=False)
            blog_post.author = request.user

            # Extract the video ID from youtube_video_url
            youtube_url = form.cleaned_data.get('youtube_video_url')
            video_id = extract_video_id(youtube_url)

            if video_id:
                # Construct the embed URL
                embed_url = f"https://www.youtube.com/embed/{video_id}"
                blog_post.youtube_video_url = embed_url

            blog_post.save()
            return redirect('blog:blog_detail', slug=blog_post.slug)
    else:
        form = BlogPostForm()

    return render(request, 'blog/add_blog_post.html', {'form': form})


def blog_home(request):
    try:
        posts = BlogPost.objects.all().order_by('-published_date')
        return render(request, 'blog/blog_home.html', {'posts': posts})
    except Exception as e:
        logging.error(f"Error in blog_home view: {e}")

def blog_detail(request, slug):
    post = get_object_or_404(BlogPost, slug=slug)
    return render(request, 'blog/blog_detail.html', {'post': post})

def skate_section(request):
    skate_subcategories = SubCategory.objects.filter(parent_category='SK')
    posts = BlogPost.objects.filter(subcategory__in=skate_subcategories).order_by('-published_date')
    return render(request, 'blog/skate_section.html', {'posts': posts})

def music_section(request):
    music_subcategories = SubCategory.objects.filter(parent_category='MU')
    posts = BlogPost.objects.filter(subcategory__in=music_subcategories).order_by('-published_date')
    return render(request, 'blog/music_section.html', {'posts': posts})

def history_section(request):
    history_subcategories = SubCategory.objects.filter(parent_category='HI')
    posts = BlogPost.objects.filter(subcategory__in=history_subcategories).order_by('-published_date')
    return render(request, 'blog/history_section.html', {'posts': posts})

def upload_image(request):
    if request.method == 'POST' and request.FILES['image']:
        try:
            # Uploading and transforming the image
            uploaded_image = request.FILES['image']
            result = cloudinary.uploader.upload(
                uploaded_image,
                crop="fill",
                gravity="face",
                width=300,
                height=300,
                secure=True  # Force HTTPS
            )

            # Get the HTTPS image URL
            image_url = result['secure_url']

            # Return the HTTPS image URL in the response
            return JsonResponse({'success': True, 'image_url': image_url})
        except Exception as e:
            # Handle any exceptions (e.g., image upload failure)
            return JsonResponse({'success': False, 'error_message': str(e)})

    # Handle other HTTP methods or no image uploaded
    return JsonResponse({'success': False, 'error_message': 'Invalid request'})


@require_POST
def like_dislike(request):
    post_id = request.POST.get('postId')
    action = request.POST.get('action')
    post = get_object_or_404(BlogPost, id=post_id)

    if request.user.is_authenticated:
        interaction, created = PostInteraction.objects.get_or_create(user=request.user, post=post)

        if action == 'like':
            interaction.liked = not interaction.liked  # Toggle like
            interaction.disliked = False if interaction.liked else interaction.disliked
        elif action == 'dislike':
            interaction.disliked = not interaction.disliked  # Toggle dislike
            interaction.liked = False if interaction.disliked else interaction.liked

        interaction.save()
    else:
        # Handle likes/dislikes from anonymous users
        if action == 'like':
            post.likes += 1
        elif action == 'dislike':
            post.dislikes += 1

        post.save()  # Save the post object

    # Refresh post to get updated counts
    post.refresh_from_db()

    return JsonResponse({
        'success': True,
        'likes': post.total_likes(),
        'dislikes': post.total_dislikes()
    })
