# Generated by Django 4.2.11 on 2024-06-11 01:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exercises', '0010_alter_exercise_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exercise',
            name='image',
            field=models.ImageField(default='exercise_image.png', upload_to='exercises/'),
        ),
    ]