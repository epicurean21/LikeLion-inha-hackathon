# Generated by Django 3.1.1 on 2020-09-17 17:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_auto_20200917_1713'),
    ]

    operations = [
        migrations.AddField(
            model_name='profilemer',
            name='title',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='profilemer',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='merchandiser'),
        ),
    ]
