# Generated by Django 4.1 on 2022-10-27 16:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_alter_phone_options_rename_phone_phone_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sitesetting',
            name='additional_about_text',
            field=models.TextField(verbose_name='توضیحات اضافی'),
        ),
    ]
