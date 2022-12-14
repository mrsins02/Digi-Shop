# Generated by Django 4.1 on 2022-10-27 16:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Phone',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Phone', models.CharField(max_length=14, verbose_name='شماره تماس')),
            ],
        ),
        migrations.CreateModel(
            name='SiteSetting',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=72, verbose_name='عنوان')),
                ('logo', models.ImageField(upload_to='media/site_logos/', verbose_name='لوگوی سایت')),
                ('address', models.TextField()),
                ('fax', models.CharField(max_length=72, verbose_name='فکس')),
                ('email', models.EmailField(max_length=72, verbose_name='ایمیل')),
                ('instagram', models.CharField(max_length=72, verbose_name='اینستاگرام')),
                ('telegram', models.CharField(max_length=72, verbose_name='تلگرام')),
                ('twitter', models.CharField(max_length=72, verbose_name='توییتر')),
                ('additional_about_text', models.TextField(max_length=72, verbose_name='توضیحات اضافی')),
                ('phone', models.ManyToManyField(to='main.phone', verbose_name='شماره تماس(ها)')),
            ],
        ),
    ]
