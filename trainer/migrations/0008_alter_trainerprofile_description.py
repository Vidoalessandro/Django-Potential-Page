# Generated by Django 4.2.11 on 2024-06-18 17:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trainer', '0007_remove_trainerprofile_customers_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trainerprofile',
            name='description',
            field=models.TextField(blank=True),
        ),
    ]
