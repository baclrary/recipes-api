# Generated by Django 3.2.4 on 2024-01-10 00:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alchemy', '0004_auto_20240108_1732'),
    ]

    operations = [
        migrations.AlterField(
            model_name='decotion',
            name='img',
            field=models.ImageField(default='assets/default_decotion.png', upload_to='alchemy/decotions/'),
        ),
    ]
