# Generated by Django 4.0.3 on 2022-06-15 11:47

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0016_alter_profile_member'),
    ]

    operations = [
        migrations.AlterField(
            
            model_name='profile',
            name='profile_picture',
            field=cloudinary.models.CloudinaryField(default='https://res.cloudinary.com/dbgbail9r/image/upload/v1649544556/profile_image_kfrlhw.png', max_length=255, verbose_name='images'),
        ),
    ]
