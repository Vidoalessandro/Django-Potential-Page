# Generated by Django 4.2.11 on 2024-06-11 00:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exercises', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exercise',
            name='image',
            field=models.ImageField(default='exercises/exercise_image.png', upload_to='exercises/'),
        ),
    ]
