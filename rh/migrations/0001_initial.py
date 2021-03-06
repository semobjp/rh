# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-13 11:29
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cargo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao_cargo', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Estado',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao_estado', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Filial',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao_filial', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Funcionario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('usuario', models.CharField(max_length=50)),
                ('senha', models.CharField(max_length=128)),
                ('nome', models.CharField(max_length=100)),
                ('nascimento', models.DateField()),
                ('cpf', models.CharField(max_length=20)),
                ('vinculo', models.CharField(choices=[('', '-'), ('Ativo', 'Ativo'), ('Desativado', 'Desativado')], max_length=50)),
                ('mae', models.CharField(max_length=100)),
                ('pai', models.CharField(max_length=100)),
                ('estado_civil', models.CharField(choices=[('', '-'), ('Solteiro', 'Solteiro'), ('Casado', 'Casado'), ('Viúvo', 'Viúvo')], max_length=50)),
                ('laudo', models.CharField(max_length=500)),
                ('rua', models.CharField(max_length=100)),
                ('numero', models.CharField(max_length=10)),
                ('bairro', models.CharField(max_length=100)),
                ('cep', models.CharField(max_length=20)),
                ('cidade', models.CharField(max_length=100)),
                ('cargo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rh.Cargo')),
                ('estado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rh.Estado')),
                ('filial', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rh.Filial')),
            ],
        ),
        migrations.CreateModel(
            name='Setor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao_setor', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='funcionario',
            name='setor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rh.Setor'),
        ),
    ]
