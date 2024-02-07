# Generated by Django 3.2.4 on 2024-02-07 14:05

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0003_auto_20240202_1222'),
    ]

    operations = [
        migrations.AlterField(
            model_name='baseitem',
            name='weight',
            field=models.FloatField(default=0, validators=[django.core.validators.MinValueValidator(0.0)]),
        ),
    ]
