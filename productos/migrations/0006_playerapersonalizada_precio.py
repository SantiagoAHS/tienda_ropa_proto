# Generated by Django 5.0.6 on 2024-11-15 01:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0005_remove_playerapersonalizada_precio'),
    ]

    operations = [
        migrations.AddField(
            model_name='playerapersonalizada',
            name='precio',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True),
        ),
    ]
