# Generated by Django 4.0.10 on 2024-07-30 04:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('consignado', '0004_alter_reserva_situacao'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reserva',
            name='situacao',
            field=models.SmallIntegerField(choices=[(0, 'EM ANALISE'), (1, 'DEFERIDO'), (2, 'INDEFERIDO'), (3, 'EXPIRADO')], default=0),
        ),
    ]
