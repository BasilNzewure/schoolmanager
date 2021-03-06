# Generated by Django 3.2.9 on 2022-01-21 18:53

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='authorbooks',
            name='name',
        ),
        migrations.AddField(
            model_name='authorbooks',
            name='author',
            field=models.CharField(default='Basil Isaac Nzewure', max_length=200, verbose_name='Author'),
        ),
        migrations.AddField(
            model_name='authorbooks',
            name='edition',
            field=models.CharField(default='11th Edition', max_length=200, verbose_name='Edition'),
        ),
        migrations.AddField(
            model_name='authorbooks',
            name='publication_yr',
            field=models.DateField(default=datetime.datetime(2022, 1, 21, 19, 53, 50, 89452), verbose_name='Publication Year'),
        ),
        migrations.AddField(
            model_name='authorbooks',
            name='publisher',
            field=models.CharField(default='Bin Binary Publishers', max_length=200, verbose_name='Publisher'),
        ),
        migrations.AlterField(
            model_name='authorbooks',
            name='title',
            field=models.CharField(max_length=200, verbose_name='Book Title'),
        ),
    ]
