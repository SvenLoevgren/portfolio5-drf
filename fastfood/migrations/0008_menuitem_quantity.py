# Generated by Django 3.2.18 on 2023-08-08 12:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fastfood', '0007_menuitem'),
    ]

    operations = [
        migrations.AddField(
            model_name='menuitem',
            name='quantity',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
