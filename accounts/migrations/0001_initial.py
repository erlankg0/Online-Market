# Generated by Django 3.2.10 on 2021-12-19 20:34

from django.db import migrations, models
import django.db.models.manager


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('first_name', models.CharField(help_text='Max 50 chars', max_length=50, verbose_name='First name')),
                ('last_name', models.CharField(help_text='Max 50 chars', max_length=50, verbose_name='Last name')),
                ('username', models.CharField(help_text='Max 100 chars', max_length=100, unique=True, verbose_name='User name')),
                ('email', models.EmailField(help_text='Max 250 chars', max_length=250, unique=True)),
                ('phone_number', models.CharField(help_text='Max 30 chars', max_length=30, verbose_name='Phone number')),
                ('data_joined', models.DateTimeField(auto_now_add=True)),
                ('last_login', models.DateTimeField(auto_now_add=True)),
                ('is_admin', models.BooleanField(default=False)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=False)),
                ('is_superadmin', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
            managers=[
                ('object', django.db.models.manager.Manager()),
            ],
        ),
    ]
