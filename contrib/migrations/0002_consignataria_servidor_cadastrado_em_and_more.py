# Generated by Django 4.0.10 on 2024-07-27 16:41

import cuser.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('contrib', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Consignataria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.AddField(
            model_name='servidor',
            name='cadastrado_em',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='servidor',
            name='cadastrado_por',
            field=cuser.fields.CurrentUserField(editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(app_label)s_%(class)s_cadastrado_por', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='servidor',
            name='desativado_em',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='servidor',
            name='desativado_por',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(app_label)s_%(class)s_desativado_por', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='servidor',
            name='modificado_em',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AddField(
            model_name='servidor',
            name='modificado_por',
            field=cuser.fields.CurrentUserField(editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(app_label)s_%(class)s_modificado_por', to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='Consulta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_Consignataria', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='consultas_consultataria', to='contrib.consignataria')),
                ('matricula', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='contrib.servidor')),
            ],
            options={
                'verbose_name': 'Consulta',
                'verbose_name_plural': 'Consultas',
            },
        ),
        migrations.AddField(
            model_name='consignataria',
            name='consulta',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='contrib.consulta'),
        ),
    ]