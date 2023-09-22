# Generated by Django 4.2 on 2023-06-10 16:12

from django.db import migrations, models
import users.models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_alter_userprofile_profile_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='profile_image',
            field=models.ImageField(blank=True, default='static/users/images/default_user_avatar.jpg', upload_to=users.models.get_user_image_path, verbose_name='Фотография'),
        ),
    ]
