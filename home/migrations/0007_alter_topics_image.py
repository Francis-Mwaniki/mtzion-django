# Generated by Django 4.1.4 on 2023-01-04 08:37

from django.db import migrations, models
import home.models


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0006_topics_image"),
    ]

    operations = [
        migrations.AlterField(
            model_name="topics",
            name="image",
            field=models.ImageField(
                default="default/car.png",
                max_length=255,
                upload_to=home.models.Topics.image_upload_to,
            ),
        ),
    ]