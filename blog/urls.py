from django.urls import path
from . import views

urlpatterns = [
    path('', views.blog_home, name='blog_home'),
    path('<slug:slug>/', views.blog_detail, name='blog_detail'),
    path('blog/skate/', views.skate_section, name='skate_section'),
    path('blog/music/', views.music_section, name='music_section'),
    path('blog/history/', views.history_section, name='history_section'),
    path('blog/like_dislike_action/', views.like_dislike_action, name='blog_like_dislike_action'),
]