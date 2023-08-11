# Generated by Django 3.2.18 on 2023-08-11 13:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('fastfood', '0010_rename_category_menuitem_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='menuitem',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
