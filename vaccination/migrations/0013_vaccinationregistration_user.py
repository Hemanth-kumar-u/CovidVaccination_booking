# Generated by Django 4.0.6 on 2023-06-24 06:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('vaccination', '0012_vaccinationregistration'),
    ]

    operations = [
        migrations.AddField(
            model_name='vaccinationregistration',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
