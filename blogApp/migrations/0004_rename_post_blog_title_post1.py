# Generated by Django 4.2.4 on 2023-08-30 13:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogApp', '0003_delete_blog_post_blog_title_post'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blog_title',
            old_name='post',
            new_name='post1',
        ),
    ]
