# Generated by Django 4.2.11 on 2024-06-11 00:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('routines', '0001_initial'),
        ('customer', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customerprofile',
            name='routines',
            field=models.ManyToManyField(blank=True, related_name='customers', to='routines.routine'),
        ),
    ]