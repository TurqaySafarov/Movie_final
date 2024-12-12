# Generated by Django 5.1.1 on 2024-09-14 23:15

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0033_discussioncomments_discussionlikes'),
    ]

    operations = [
        migrations.CreateModel(
            name='DiscussionCommentLikes',
            fields=[
                ('discussion_comment_like_id', models.AutoField(primary_key=True, serialize=False)),
                ('discussion_comment', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='app.discussioncomments')),
                ('user', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='app.usersapp')),
            ],
        ),
    ]
