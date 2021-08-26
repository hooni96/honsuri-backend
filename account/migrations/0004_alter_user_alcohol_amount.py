# Generated by Django 3.2.6 on 2021-08-23 07:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_alter_user_alcohol_amount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='alcohol_amount',
            field=models.CharField(blank=True, choices=[('1잔 ~ 4잔', '1잔 ~ 4잔'), ('5잔 ~ 1.5병', '5잔 ~ 1.5병'), ('1.5병 ~ 2.5병', '1.5병 ~ 2.5병'), ('2.5병 ~ 5병 이상', '2.5병 ~ 5병 이상')], max_length=32, null=True),
        ),
    ]