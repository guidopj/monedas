# Generated by Django 2.1 on 2018-08-13 03:54

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('monedas', '0004_auto_20180812_2354'),
    ]

    operations = [
        migrations.AddField(
            model_name='historial',
            name='accion',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='last_login',
            field=models.DateField(default=datetime.datetime(2018, 8, 13, 3, 54, 51, 356020)),
        ),
    ]
