from django.urls import path

from . import views

app_name = "blog"

urlpatterns = [
    path("", views.blog_home, name="blog_home"),
    path("skate/", views.skate_section, name="skate_section"),
    path("music_section/", views.music_section, name="music_section"),
    path("history_section/", views.history_section, name="history_section"),
    path("add/", views.add_blog_post, name="add_blog_post"),
    path("like_dislike/", views.like_dislike, name="like_dislike"),
    path("<slug:slug>/", views.blog_detail, name="blog_detail"),
]
