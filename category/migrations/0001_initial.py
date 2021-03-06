# Generated by Django 3.2.10 on 2021-12-19 19:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=100, verbose_name='Category')),
                ('slug', models.CharField(max_length=256, unique=True, verbose_name='url')),
                ('description', models.TextField(blank=True, max_length=255, verbose_name='Description')),
                ('category_image', models.ImageField(blank=True, upload_to='photos/categories')),
            ],
        ),
    ]
