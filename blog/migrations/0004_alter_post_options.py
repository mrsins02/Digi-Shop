# Generated by Django 4.1 on 2022-10-28 22:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_alter_post_options_alter_post_author'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ('-created',), 'verbose_name': 'پست', 'verbose_name_plural': 'پست ها'},
        ),
    ]