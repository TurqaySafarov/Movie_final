# Generated by Django 5.1.1 on 2024-09-06 20:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Film',
            fields=[
                ('film_id', models.AutoField(primary_key=True, serialize=False)),
                ('film_name', models.CharField(max_length=100)),
                ('film_director', models.CharField(max_length=100)),
                ('film_category', models.CharField(max_length=100)),
                ('film_genre', models.CharField(max_length=100)),
                ('film_release_date', models.DateField()),
                ('film_duration', models.DurationField()),
                ('film_description', models.TextField()),
                ('film_cast', models.JSONField()),
            ],
        ),
    ]
