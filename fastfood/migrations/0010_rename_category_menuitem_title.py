# Generated by Django 3.2.18 on 2023-08-08 12:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fastfood', '0009_alter_menuitem_description'),
    ]

    operations = [
        migrations.RenameField(
            model_name='menuitem',
            old_name='category',
            new_name='title',
        ),
    ]
