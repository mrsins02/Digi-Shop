# Generated by Django 4.1 on 2022-08-30 16:07

from django.db import migrations, models
import products.models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_product_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='default_picture',
            field=models.ImageField(blank=True, null=True, upload_to=products.models.product_name_generator, verbose_name='عکس پیش فرض'),
        ),
    ]
