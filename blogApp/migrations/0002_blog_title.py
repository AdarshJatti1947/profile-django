# Generated by Django 4.2.4 on 2023-08-29 19:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog_title',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post_title', models.TextField(max_length=20)),
            ],
        ),
    ]
