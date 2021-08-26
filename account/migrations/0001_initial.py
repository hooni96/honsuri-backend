# Generated by Django 3.2.6 on 2021-08-26 13:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('email', models.EmailField(max_length=255, unique=True)),
                ('name', models.CharField(max_length=40)),
                ('nickname', models.CharField(max_length=40, unique=True)),
                ('phone_number', models.CharField(max_length=12)),
                ('alcohol_amount', models.FloatField(blank=True)),
                ('favorite_alcohol', models.CharField(blank=True, max_length=40)),
                ('favorite_food', models.CharField(blank=True, max_length=40)),
                ('favorite_combination', models.CharField(blank=True, max_length=40)),
                ('is_active', models.BooleanField(default=True)),
                ('is_admin', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
