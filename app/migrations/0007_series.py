# Generated by Django 5.1.1 on 2024-09-06 21:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_film_film_link'),
    ]

    operations = [
        migrations.CreateModel(
            name='Series',
            fields=[
                ('series_id', models.AutoField(primary_key=True, serialize=False)),
                ('series_name', models.CharField(max_length=100)),
                ('series_director', models.CharField(max_length=100)),
                ('series_category', models.CharField(max_length=100)),
                ('series_genre', models.CharField(max_length=100)),
                ('series_release_date', models.DateField()),
                ('series_duration', models.DurationField()),
                ('series_description', models.TextField()),
                ('series_poster', models.ImageField(default='', upload_to='series_posters/')),
                ('series_trailer', models.URLField(default='')),
                ('series_video', models.FileField(default='', upload_to='series_videos/')),
                ('series_cast', models.JSONField()),
                ('series_imdb_rating', models.FloatField(default=0.0)),
            ],
        ),
    ]