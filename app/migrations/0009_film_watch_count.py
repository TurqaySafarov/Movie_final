# Generated by Django 5.1.1 on 2024-09-09 16:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_film_movie_open_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='film',
            name='watch_count',
            field=models.IntegerField(default=0),
        ),
    ]