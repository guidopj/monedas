# Generated by Django 2.1 on 2018-08-04 18:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Moneda',
            fields=[
                ('nombreMoneda', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('signo', models.CharField(max_length=8)),
            ],
        ),
        migrations.CreateModel(
            name='MonedasUsuario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantMonedas', models.IntegerField()),
                ('nombreMoneda', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='monedas.Moneda')),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('nombreUsuario', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=100)),
                ('apellido', models.CharField(max_length=100)),
                ('fecha_nac', models.DateTimeField()),
            ],
        ),
        migrations.AddField(
            model_name='monedasusuario',
            name='nombreUsuario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='monedas.Usuario'),
        ),
        migrations.AddField(
            model_name='moneda',
            name='creadaPor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='monedas.Usuario'),
        ),
    ]
