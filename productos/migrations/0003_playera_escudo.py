# Generated by Django 5.0.6 on 2024-11-15 00:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0002_playera_color_personalizado_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='playera',
            name='escudo',
            field=models.ImageField(blank=True, null=True, upload_to='escudos/'),
        ),
    ]
