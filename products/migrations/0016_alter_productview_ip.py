# Generated by Django 4.1.3 on 2022-12-11 21:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0015_productview'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productview',
            name='ip',
            field=models.CharField(max_length=32),
        ),
    ]