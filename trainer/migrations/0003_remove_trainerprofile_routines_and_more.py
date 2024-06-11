# Generated by Django 4.2.11 on 2024-06-10 23:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('routines', '0001_initial'),
        ('trainer', '0002_alter_trainerprofile_customers_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='trainerprofile',
            name='routines',
        ),
        migrations.AddField(
            model_name='trainerprofile',
            name='routines',
            field=models.ManyToManyField(blank=True, related_name='trainer', to='routines.routine'),
        ),
    ]