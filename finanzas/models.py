from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Moneda(models.Model):
    moneda=models.TextField(max_length=100)

    def __unicode__(self):
        return self.moneda

class Acreedor(models.Model):
    codigo=models.CharField(max_length=100)
    descripcion=models.TextField(max_length=100)

    def __unicode__(self):
        return self.id

class Cobro(models.Model):
    numero_factura=models.CharField(max_length=100)
    contrato=models.CharField(max_length=100)
    cuenta=models.CharField(max_length=100)
    fecha_contabilidad=models.DateField(max_length=100)
    monto_cuc=models.CharField(max_length=100)
    monto_cup=models.CharField(max_length=100)
    moneda=models.CharField(max_length=100)
    monto_moneda=models.CharField(max_length=100)

    def __unicode__(self):
        return self.numero_factura

class Deudor(models.Model):
    codigo=models.CharField(max_length=100)
    descripcion=models.TextField(max_length=100)

    def __unicode__(self):
        return self.id

class Pago(models.Model):
    numero_factura=models.CharField(max_length=100)
    contrato=models.CharField(max_length=100)
    cuenta=models.CharField(max_length=100)
    fecha_contabilidad=models.DateField(max_length=100)
    monto_cuc=models.CharField(max_length=100)
    monto_cup=models.CharField(max_length=100)
    moneda=models.CharField(max_length=100)
    monto_moneda=models.CharField(max_length=100)

    def __unicode__(self):
        return self.id

class Plan_Cuentas(models.Model):
    cuenta=models.CharField(max_length=100)
    subcuenta=models.CharField(max_length=100)
    nivel1=models.CharField(max_length=100)
    nivel2=models.CharField(max_length=100)
    nivel3=models.CharField(max_length=100)
    nivel4=models.CharField(max_length=100)
    subcuenta=models.BooleanField(max_length=100)

    def __unicode__(self):
        return self.id

class Registro(models.Model):
    cuenta=models.CharField(max_length=100)
    acredor_deudor=models.CharField(max_length=100)
    usuario=models.CharField(max_length=100)
    fecha_contabilidad=models.DateField(max_length=100)
    monto_cuc=models.CharField(max_length=100)
    monto_cup=models.CharField(max_length=100)
    moneda=models.CharField(max_length=100)
    monto_moneda=models.CharField(max_length=100)
    contrato=models.CharField(max_length=100)
    nro_factura=models.CharField(max_length=100)
    fecha_pago=models.DateField()
    observaciones=models.CharField(max_length=100)
