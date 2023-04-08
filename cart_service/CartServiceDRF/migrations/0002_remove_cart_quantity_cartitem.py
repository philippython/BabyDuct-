# Generated by Django 4.1.7 on 2023-04-01 11:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('CartServiceDRF', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='quantity',
        ),
        migrations.CreateModel(
            name='CartItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField()),
                ('price', models.PositiveIntegerField()),
                ('name', models.CharField(max_length=255)),
                ('cart', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CartServiceDRF.cart')),
            ],
        ),
    ]