# Generated by Django 4.1 on 2024-03-24 11:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("cinema", "0003_alter_movie_image"),
    ]

    operations = [
        migrations.AlterField(
            model_name="movie",
            name="image",
            field=models.ImageField(null=True, upload_to="movie_image_path"),
        ),
    ]
