# Generated by Django 4.2.9 on 2024-01-08 11:25

import django_countries.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("checkout", "0002_order_original_bag_order_stripe_pid"),
    ]

    operations = [
        migrations.AlterField(
            model_name="order",
            name="country",
            field=django_countries.fields.CountryField(max_length=2),
        ),
    ]
