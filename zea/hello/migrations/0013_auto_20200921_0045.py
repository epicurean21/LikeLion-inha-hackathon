# Generated by Django 3.1.1 on 2020-09-20 15:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hello', '0012_auto_20200920_0615'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='category',
            field=models.CharField(choices=[('업체', '업체'), ('학생', '학생'), ('기타', '기타')], default='업체', max_length=10),
        ),
    ]