# Generated by Django 4.1 on 2022-08-29 20:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_remove_product_test'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='price',
            field=models.IntegerField(default=0, max_length=20, verbose_name='قیمت'),
            preserve_default=False,
        ),
    ]
