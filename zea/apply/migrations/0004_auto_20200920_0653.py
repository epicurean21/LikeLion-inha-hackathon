# Generated by Django 3.1.1 on 2020-09-20 06:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('apply', '0003_auto_20200919_0916'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='merchandiserapply',
            name='file',
        ),
        migrations.RemoveField(
            model_name='merchandiserapply',
            name='title',
        ),
        migrations.RemoveField(
            model_name='merchandiserapply',
            name='user',
        ),
    ]