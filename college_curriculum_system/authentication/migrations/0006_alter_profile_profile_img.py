# Generated by Django 5.0.2 on 2024-07-31 09:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0005_profile_profile_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_img',
            field=models.ImageField(default='default_profille_photo.png', upload_to='user_images/'),
        ),
    ]