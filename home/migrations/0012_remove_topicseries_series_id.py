# Generated by Django 4.1.4 on 2023-01-04 11:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0011_topicseries_series_id"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="topicseries",
            name="series_id",
        ),
    ]
