# Generated by Django 5.0.7 on 2024-07-24 02:05

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('consignataria', '0001_initial'),
        ('contrib', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ConsultaMargemAthena',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('margem_total', models.DecimalField(decimal_places=2, max_digits=10)),
                ('margem_disponivel', models.DecimalField(decimal_places=2, max_digits=10)),
                ('consignataria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='consignataria.consignataria')),
                ('servidor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contrib.servidor')),
            ],
        ),
        migrations.CreateModel(
            name='Reserva',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('valor', models.DecimalField(decimal_places=2, max_digits=10)),
                ('prazo_inicial', models.DateTimeField()),
                ('prazo_final', models.DateTimeField()),
                ('situacao', models.IntegerField()),
                ('contrato', models.CharField(max_length=255, unique=True)),
                ('consulta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='consignado.consultamargemathena')),
            ],
        ),
    ]