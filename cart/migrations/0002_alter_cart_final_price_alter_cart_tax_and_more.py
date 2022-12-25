# Generated by Django 4.1.3 on 2022-12-17 20:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0016_alter_productview_ip'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('cart', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='final_price',
            field=models.IntegerField(blank=True, default=0, verbose_name=''),
        ),
        migrations.AlterField(
            model_name='cart',
            name='tax',
            field=models.IntegerField(blank=True, null=True, verbose_name=''),
        ),
        migrations.AlterField(
            model_name='cart',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name=''),
        ),
        migrations.AlterField(
            model_name='cartproducts',
            name='cart',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cart.cart', verbose_name=''),
        ),
        migrations.AlterField(
            model_name='cartproducts',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.product', verbose_name=''),
        ),
        migrations.AlterField(
            model_name='cartproducts',
            name='product_final_price',
            field=models.IntegerField(blank=True, null=True, verbose_name=''),
        ),
        migrations.AlterField(
            model_name='cartproducts',
            name='product_price',
            field=models.IntegerField(blank=True, null=True, verbose_name=''),
        ),
    ]