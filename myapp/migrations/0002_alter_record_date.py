# Generated by Django 5.2.2 on 2025-06-07 17:34

import django.utils.timezone
from django.db import migrations

import myapp.models


class Migration(migrations.Migration):
    dependencies = [
        ("myapp", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="record",
            name="date",
            field=myapp.models.TimestampField(default=django.utils.timezone.now),
        ),
    ]
