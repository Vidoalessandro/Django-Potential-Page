# Generated by Django 4.2.11 on 2024-06-11 01:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trainer', '0003_remove_trainerprofile_routines_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trainerprofile',
            name='profile_picture',
            field=models.ImageField(default='users/user_image.png', upload_to='users/'),
        ),
    ]
