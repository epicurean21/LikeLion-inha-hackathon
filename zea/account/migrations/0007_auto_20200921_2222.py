# Generated by Django 3.1.1 on 2020-09-21 13:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0006_auto_20200920_2032'),
    ]

    operations = [
        migrations.AddField(
            model_name='profilemer',
            name='category',
            field=models.CharField(choices=[('업체', '업체'), ('학생', '학생'), ('기타', '기타')], default='업체', max_length=10),
        ),
        migrations.AddField(
            model_name='profilestu',
            name='category',
            field=models.CharField(choices=[('업체', '업체'), ('학생', '학생'), ('기타', '기타')], default='업체', max_length=10),
        ),
    ]
