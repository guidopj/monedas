# Generated by Django 2.1 on 2018-08-08 01:07

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('monedas', '0004_historial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='moneda',
            name='fechaCreacion',
            field=models.DateField(default=datetime.datetime.now),
        ),
    ]