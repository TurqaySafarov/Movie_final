# Generated by Django 5.1.1 on 2024-09-14 22:01

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0031_discussion'),
    ]

    operations = [
        migrations.AddField(
            model_name='discussion',
            name='discussion_film',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='app.film'),
        ),
    ]
