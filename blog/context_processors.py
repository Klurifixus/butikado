from .models import BlogPost

def latest_posts(request):
    latest_posts = BlogPost.objects.order_by('-published_date')[:5]  # Adjust the number as needed
    return {'latest_posts': latest_posts}