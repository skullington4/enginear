# Generated by Django 4.1.7 on 2023-03-17 20:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_rename_posts_post'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='engineer',
        ),
    ]