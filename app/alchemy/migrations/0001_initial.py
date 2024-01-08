# Generated by Django 3.2.4 on 2024-01-07 17:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bomb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500)),
                ('price', models.PositiveIntegerField()),
                ('source', models.CharField(max_length=2000)),
                ('link', models.CharField(blank=True, max_length=2000, null=True)),
                ('effect', models.CharField(max_length=2000)),
                ('charges', models.PositiveSmallIntegerField(default=1)),
                ('duration_sec', models.PositiveIntegerField(default=1800)),
                ('img', models.ImageField(default='media/assets/bomb_default.png', upload_to='alchemy/bombs/')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Decotion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500)),
                ('price', models.PositiveIntegerField()),
                ('source', models.CharField(max_length=2000)),
                ('link', models.CharField(blank=True, max_length=2000, null=True)),
                ('effect', models.CharField(max_length=2000)),
                ('img', models.ImageField(default='media/assets/decotion_default.png', upload_to='alchemy/decotions/')),
                ('charges', models.PositiveSmallIntegerField(default=1)),
                ('duration_sec', models.PositiveIntegerField(default=1800)),
                ('tox_points', models.PositiveSmallIntegerField(default=50)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Oil',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500)),
                ('price', models.PositiveIntegerField()),
                ('source', models.CharField(max_length=2000)),
                ('link', models.CharField(blank=True, max_length=2000, null=True)),
                ('effect', models.CharField(max_length=2000)),
                ('img', models.ImageField(default='media/assets/oil_default.png', upload_to='alchemy/oils/')),
                ('charges', models.PositiveSmallIntegerField(default=30)),
                ('attack_bonus_perc', models.PositiveSmallIntegerField(default=15)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Potion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500)),
                ('price', models.PositiveIntegerField()),
                ('source', models.CharField(max_length=2000)),
                ('link', models.CharField(blank=True, max_length=2000, null=True)),
                ('effect', models.CharField(max_length=2000)),
                ('img', models.ImageField(default='media/assets/potion_default.png', upload_to='alchemy/potions/')),
                ('charges', models.PositiveSmallIntegerField(default=3)),
                ('duration_sec', models.PositiveIntegerField(default=30)),
                ('tox_points', models.PositiveSmallIntegerField(default=20)),
                ('tier', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='core.tier')),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='core.type')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
