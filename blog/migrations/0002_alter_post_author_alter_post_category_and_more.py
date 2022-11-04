# Generated by Django 4.1 on 2022-10-28 20:33

import blog.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='نویسنده'),
        ),
        migrations.AlterField(
            model_name='post',
            name='category',
            field=models.ManyToManyField(to='blog.category', verbose_name='دسته بندی'),
        ),
        migrations.AlterField(
            model_name='post',
            name='english_title',
            field=models.CharField(max_length=128, verbose_name='عنوان انگلیسی'),
        ),
        migrations.AlterField(
            model_name='post',
            name='is_active',
            field=models.BooleanField(default=True, verbose_name='فعال/غیرفعال'),
        ),
        migrations.AlterField(
            model_name='post',
            name='picture',
            field=models.ImageField(upload_to=blog.models.post_name_generator, verbose_name='عکس'),
        ),
        migrations.AlterField(
            model_name='post',
            name='slug',
            field=models.SlugField(editable=False, max_length=128),
        ),
        migrations.AlterField(
            model_name='post',
            name='text',
            field=models.TextField(verbose_name='متن پست'),
        ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(max_length=128, verbose_name='عنوان'),
        ),
    ]
