# Generated by Django 4.1.7 on 2024-01-18 16:03

import core.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Programs",
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
                (
                    "title",
                    models.CharField(max_length=500, verbose_name="Program Title"),
                ),
                ("body_intro", models.TextField(default="Type here...")),
                ("published_date", models.DateField(auto_now_add=True)),
                ("updated_datetime", models.DateTimeField(auto_now=True)),
                (
                    "priority_in_home",
                    models.IntegerField(
                        blank=True,
                        default=0,
                        validators=[core.models.validate_if_between_1_3],
                    ),
                ),
                ("priority_in_programs", models.IntegerField(default=0)),
                (
                    "featured_image",
                    models.ImageField(
                        blank=True,
                        default="default/no_image.jpg",
                        null=True,
                        upload_to="images/test_uploads/",
                    ),
                ),
                ("slug", models.SlugField(max_length=600, unique=True)),
            ],
        ),
        migrations.AlterField(
            model_name="contact",
            name="phone",
            field=models.CharField(default="", max_length=20),
        ),
    ]
