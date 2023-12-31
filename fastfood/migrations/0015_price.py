# Generated by Django 3.2.18 on 2023-08-11 19:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('fastfood', '0014_alter_menuitem_price'),
    ]

    operations = [
        migrations.CreateModel(
            name='Price',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('item', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='price_relation', to='fastfood.menuitem')),
            ],
        ),
    ]
