# Generated by Django 4.1.3 on 2022-12-17 21:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0003_alter_cart_options_alter_cartproducts_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cartproducts',
            name='product_final_price',
            field=models.IntegerField(blank=True, default=0, verbose_name='قیمت نهایی محصول'),
        ),
        migrations.AlterField(
            model_name='cartproducts',
            name='product_price',
            field=models.IntegerField(blank=True, default=0, verbose_name='قیمت محصول'),
        ),
    ]