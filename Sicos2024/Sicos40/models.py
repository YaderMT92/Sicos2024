from django.db import models

# Create your models here.
class Cliente(models.Model):
    IdCliente = models.BigAutoField(primary_key=True)
    Nombres = models.CharField(max_length=50)
    Apellidos = models.CharField(max_length=80)
    cedula = models.CharField(max_length=15)
    LugarTrabajo = models.CharField(max_length=100)
    Direccion = models.CharField(max_length=100)
    TipoId = models.CharField(max_length=3)
    SujetoObligado = models.CharField(max_length=2)
    Categoria = models.CharField(max_length=10)
    
    class Meta:
        db_table = 'tblclientes' 

class Poliza(models.Model):
    IdPoliza = models.BigAutoField(primary_key=True)
    NumeroPoliza = models.CharField(max_length=50)
    desde = models.CharField(max_length=15)
    hasta = models.CharField(max_length=15)
    IdCliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, db_column='IdCliente')

    class Meta:
        db_table = 'tblpolizas'