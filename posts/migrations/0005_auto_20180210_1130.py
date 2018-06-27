# Generated by Django 2.0.2 on 2018-02-10 09:30

import accounts.names
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0004_auto_20180209_1624'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='image',
            field=models.ImageField(blank=True, default=accounts.names.generate_random_pic, null=True, upload_to='whisper_images/'),
        ),
        migrations.AlterField(
            model_name='whisper',
            name='image',
            field=models.ImageField(blank=True, default=accounts.names.generate_random_pic, null=True, upload_to='whisper_images/'),
        ),
    ]