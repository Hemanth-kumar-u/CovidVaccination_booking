# Generated by Django 4.0.6 on 2023-06-24 10:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vaccination', '0015_vaccinationcentre_dosages_available_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vaccinationcentre',
            name='working_hours',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]