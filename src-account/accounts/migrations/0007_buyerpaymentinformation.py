# Generated by Django 4.0.6 on 2023-03-17 23:00

import accounts.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_buyershipmentaddress_sellerprofile_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='BuyerPaymentInformation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('card_name', models.CharField(max_length=55)),
                ('card_number', models.CharField(max_length=16)),
                ('cvv', models.CharField(max_length=3)),
                ('payment_method', models.CharField(max_length=10)),
                ('expiry_date', models.CharField(max_length=16, validators=[accounts.models.BuyerPaymentInformation.validate_expiry_date])),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
