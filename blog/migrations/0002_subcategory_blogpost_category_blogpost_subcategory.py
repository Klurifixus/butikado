# Generated by Django 4.2.9 on 2024-01-21 10:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SubCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('parent_category', models.CharField(choices=[('SK', 'Skate'), ('MU', 'Music'), ('HI', 'History')], max_length=2)),
            ],
        ),
        migrations.AddField(
            model_name='blogpost',
            name='category',
            field=models.CharField(choices=[('SK', 'Skate'), ('MU', 'Music'), ('HI', 'History')], default='SK', max_length=2),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='blogpost',
            name='subcategory',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='blog.subcategory'),
        ),
    ]
