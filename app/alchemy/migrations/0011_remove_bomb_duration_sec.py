# Generated by Django 3.2.4 on 2024-01-10 21:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('alchemy', '0010_auto_20240110_2121'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bomb',
            name='duration_sec',
        ),
    ]