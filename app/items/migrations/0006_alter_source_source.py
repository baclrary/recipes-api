# Generated by Django 3.2.4 on 2024-02-07 16:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0005_alter_source_source'),
    ]

    operations = [
        migrations.AlterField(
            model_name='source',
            name='source',
            field=models.CharField(max_length=400, unique=True),
        ),
    ]
