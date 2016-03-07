# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Acreedor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('codigo', models.TextField()),
                ('descripcion', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Cobro',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('numero_factura', models.TextField()),
                ('contrato', models.TextField()),
                ('cuenta', models.TextField()),
                ('fecha_contabilidad', models.DateField()),
                ('monto_cuc', models.TextField()),
                ('monto_cup', models.TextField()),
                ('moneda', models.TextField()),
                ('monto_moneda', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Deudor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('codigo', models.TextField()),
                ('descripcion', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Moneda',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('moneda', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Pago',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('numero_factura', models.TextField()),
                ('contrato', models.TextField()),
                ('cuenta', models.TextField()),
                ('fecha_contabilidad', models.DateField()),
                ('monto_cuc', models.TextField()),
                ('monto_cup', models.TextField()),
                ('moneda', models.TextField()),
                ('monto_moneda', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Plan_Cuentas',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('cuenta', models.TextField()),
                ('nivel1', models.TextField()),
                ('nivel2', models.TextField()),
                ('nivel3', models.TextField()),
                ('nivel4', models.TextField()),
                ('subcuenta', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Registro',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('cuenta', models.TextField()),
                ('acredor_deudor', models.TextField()),
                ('usuario', models.TextField()),
                ('fecha_contabilidad', models.DateField()),
                ('monto_cuc', models.TextField()),
                ('monto_cup', models.TextField()),
                ('moneda', models.TextField()),
                ('monto_moneda', models.TextField()),
                ('contrato', models.TextField()),
                ('nro_factura', models.TextField()),
                ('fecha_pago', models.DateField()),
                ('observaciones', models.TextField()),
            ],
        ),
    ]
