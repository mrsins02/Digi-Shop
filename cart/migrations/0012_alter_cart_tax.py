# Generated by Django 4.1.3 on 2022-12-25 12:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0011_alter_cart_is_paid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='tax',
            field=models.IntegerField(blank=True, default=0, verbose_name='مالیات'),
        ),
    ]