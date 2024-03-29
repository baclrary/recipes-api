# Generated by Django 3.2.4 on 2024-02-02 12:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0002_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bomb',
            name='img',
            field=models.ImageField(default='assets/alchemy/default_bomb.png', null=True, upload_to='uploads/items/alchemy/decotions/'),
        ),
        migrations.AlterField(
            model_name='craftingcomponent',
            name='img',
            field=models.ImageField(default='assets/items/default_craft_component.png', null=True, upload_to='uploads/items/general/craft_components/'),
        ),
        migrations.AlterField(
            model_name='decotion',
            name='img',
            field=models.ImageField(default='assets/alchemy/default_decotion.png', null=True, upload_to='uploads/items/alchemy/decotions/'),
        ),
        migrations.AlterField(
            model_name='oil',
            name='img',
            field=models.ImageField(default='assets/alchemy/default_oil.png', null=True, upload_to='uploads/items/alchemy/oils/'),
        ),
        migrations.AlterField(
            model_name='potion',
            name='img',
            field=models.ImageField(default='assets/alchemy/default_potion.png', null=True, upload_to='uploads/items/alchemy/potions/'),
        ),
    ]
