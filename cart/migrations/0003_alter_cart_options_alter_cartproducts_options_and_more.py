# Generated by Django 4.1.3 on 2022-12-17 21:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('products', '0016_alter_productview_ip'),
        ('cart', '0002_alter_cart_final_price_alter_cart_tax_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='cart',
            options={'verbose_name': 'سبد خرید', 'verbose_name_plural': 'سبد های خرید'},
        ),
        migrations.AlterModelOptions(
            name='cartproducts',
            options={'verbose_name': 'محصول سبد خرید', 'verbose_name_plural': 'محصولات سبد خرید'},
        ),
        migrations.RemoveField(
            model_name='cartproducts',
            name='cart',
        ),
        migrations.AddField(
            model_name='cartproducts',
            name='cart_object',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='cart.cart', verbose_name='سبد خرید'),
        ),
        migrations.AlterField(
            model_name='cart',
            name='final_price',
            field=models.IntegerField(blank=True, default=0, verbose_name='قیمت نهایی'),
        ),
        migrations.AlterField(
            model_name='cart',
            name='tax',
            field=models.IntegerField(blank=True, null=True, verbose_name='مالیات'),
        ),
        migrations.AlterField(
            model_name='cart',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='کاربر'),
        ),
        migrations.AlterField(
            model_name='cartproducts',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.product', verbose_name='محصول'),
        ),
        migrations.AlterField(
            model_name='cartproducts',
            name='product_final_price',
            field=models.IntegerField(blank=True, null=True, verbose_name='قیمت نهایی محصول'),
        ),
        migrations.AlterField(
            model_name='cartproducts',
            name='product_price',
            field=models.IntegerField(blank=True, null=True, verbose_name='قیمت محصول'),
        ),
    ]