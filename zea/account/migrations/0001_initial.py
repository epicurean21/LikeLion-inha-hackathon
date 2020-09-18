# Generated by Django 3.1.1 on 2020-09-17 16:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ProfileStu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userEmail', models.EmailField(max_length=254, unique=True)),
                ('nickName', models.TextField(max_length=15)),
                ('userSchool', models.TextField(max_length=30)),
                ('userMajor', models.TextField(max_length=50)),
                ('userGrade', models.IntegerField(default=1)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ProfileMer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userEmail', models.EmailField(max_length=254, unique=True)),
                ('nickName', models.TextField(max_length=15)),
                ('userMerchendise', models.TextField(max_length=254)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
