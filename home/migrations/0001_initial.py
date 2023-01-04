# Generated by Django 4.1.4 on 2023-01-04 18:21

from django.db import migrations, models
import django.utils.timezone
import home.models
import tinymce.models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Topics",
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
                ("title", models.CharField(max_length=255)),
                ("subtitle", models.CharField(blank=True, default="", max_length=255)),
                ("speaker", models.CharField(max_length=255)),
                ("content", tinymce.models.HTMLField(blank=True, default="")),
                (
                    "topic_slug",
                    models.SlugField(unique=True, verbose_name="Topic slug"),
                ),
                (
                    "image",
                    models.ImageField(
                        default="default/car.png",
                        max_length=255,
                        upload_to=home.models.Topics.image_upload_to,
                    ),
                ),
                (
                    "published",
                    models.DateTimeField(
                        default=django.utils.timezone.now, verbose_name="Date published"
                    ),
                ),
                (
                    "modified",
                    models.DateTimeField(
                        default=django.utils.timezone.now, verbose_name="Date modified"
                    ),
                ),
            ],
            options={
                "verbose_name_plural": "TOPICS",
                "ordering": ["-published"],
            },
        ),
        migrations.CreateModel(
            name="TopicSeries",
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
                ("title", models.CharField(max_length=255)),
                ("subtitle", models.CharField(max_length=255)),
                (
                    "slug",
                    models.SlugField(
                        null=True, unique=True, verbose_name="Topic series"
                    ),
                ),
                (
                    "image",
                    models.ImageField(
                        default="default/car.png",
                        max_length=255,
                        upload_to=home.models.TopicSeries.image_upload_to,
                    ),
                ),
                (
                    "published",
                    models.DateField(
                        default=django.utils.timezone.now, verbose_name="Date published"
                    ),
                ),
            ],
            options={
                "verbose_name_plural": "SERIES",
                "ordering": ["-published"],
            },
        ),
    ]
