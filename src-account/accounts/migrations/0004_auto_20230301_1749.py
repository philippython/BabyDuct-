# Generated by Django 3.2.3 on 2023-03-01 16:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_auto_20221224_2258'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='consumerprofile',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='consumerprofile',
            name='last_name',
        ),
        migrations.RemoveField(
            model_name='consumerprofile',
            name='profile_image',
        ),
        migrations.RemoveField(
            model_name='producerprofile',
            name='business_certificate',
        ),
        migrations.RemoveField(
            model_name='producerprofile',
            name='store_email',
        ),
        migrations.RemoveField(
            model_name='producerprofile',
            name='store_logo',
        ),
        migrations.RemoveField(
            model_name='producerprofile',
            name='store_name',
        ),
        migrations.AddField(
            model_name='producerprofile',
            name='cac_reg_no',
            field=models.CharField(default='00000000000', max_length=20),
        ),
        migrations.AddField(
            model_name='producerprofile',
            name='product_category',
            field=models.CharField(choices=[('toys', 'toys'), ('foods', 'foods'), ('cosmetics', 'cosmetics'), ('fashion', 'fashion')], default='unknown', max_length=9),
        ),
        migrations.AlterField(
            model_name='producerprofile',
            name='location',
            field=models.CharField(default='unknwown', max_length=150),
        ),
    ]
