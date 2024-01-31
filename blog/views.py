from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from .models import BlogPost, SubCategory, PostInteraction
from django.views.decorators.http import require_POST
import cloudinary.uploader
import logging


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
        # Uploading and transforming the image
        uploaded_image = request.FILES['image']
        result = cloudinary.uploader.upload(
            uploaded_image,
            crop="fill",
            gravity="face",
            width=300,
            height=300
        )


@require_POST
def like_dislike(request):
    post_id = request.POST.get('postId')
    action = request.POST.get('action')
    post = get_object_or_404(BlogPost, id=post_id)

    if request.user.is_authenticated:
        # Handle likes/dislikes from authenticated users
        interaction, created = PostInteraction.objects.get_or_create(user=request.user, post=post)

        if action == 'like':
            interaction.liked = not interaction.liked
            interaction.disliked = False if interaction.liked else interaction.disliked
        elif action == 'dislike':
            interaction.disliked = not interaction.disliked
            interaction.liked = False if interaction.disliked else interaction.liked

        interaction.save()
    else:
        # Handle likes/dislikes from anonymous users
        if action == 'like':
            post.likes += 1
        elif action == 'dislike':
            post.dislikes += 1

    post.save()
    return JsonResponse({'success': True, 'likes': post.likes, 'dislikes': post.dislikes})
