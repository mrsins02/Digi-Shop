# Generated by Django 4.1.3 on 2022-12-11 11:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_newsletter'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newsletter',
            name='email',
            field=models.EmailField(max_length=254, unique=True),
        ),
    ]
