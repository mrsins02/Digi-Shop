# Generated by Django 4.1.3 on 2022-12-17 22:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0009_cartproducts_total_price'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cart',
            old_name='final_price',
            new_name='total_price',
        ),
    ]
