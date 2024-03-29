# Generated by Django 4.2.9 on 2024-01-21 11:54

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("blog", "0002_subcategory_blogpost_category_blogpost_subcategory"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="blogpost",
            name="category",
        ),
        migrations.AddField(
            model_name="blogpost",
            name="author",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AddField(
            model_name="blogpost",
            name="dislikes",
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name="blogpost",
            name="image",
            field=models.ImageField(
                blank=True, null=True, upload_to="blog_images/"),
        ),
        migrations.AddField(
            model_name="blogpost",
            name="likes",
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name="blogpost",
            name="content",
            field=models.TextField(max_length=10000),
        ),
        migrations.CreateModel(
            name="PostInteraction",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("liked", models.BooleanField(default=False)),
                ("disliked", models.BooleanField(default=False)),
                (
                    "post",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="blog.blogpost"
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
