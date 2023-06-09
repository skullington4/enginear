# Generated by Django 4.1.7 on 2023-03-21 13:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main_app', '0004_remove_post_comments'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='comments',
            field=models.ManyToManyField(to='main_app.comment'),
        ),
        migrations.AddField(
            model_name='post',
            name='engineer',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='posts_engineer', to=settings.AUTH_USER_MODEL),
        ),
    ]
