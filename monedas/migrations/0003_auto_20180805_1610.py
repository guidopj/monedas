# Generated by Django 2.1 on 2018-08-05 16:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('monedas', '0002_auto_20180805_1329'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='contrasena',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='monedasusuario',
            name='cantMonedas',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='fecha_nac',
            field=models.DateField(),
        ),
    ]