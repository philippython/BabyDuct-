# Generated by Django 4.1.7 on 2023-04-01 11:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CartServiceDRF', '0002_remove_cart_quantity_cartitem'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cartitem',
            name='quantity',
            field=models.PositiveIntegerField(default=1),
        ),
    ]