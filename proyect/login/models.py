from django.db import models




class Usuarios(models.Model):
    id = models.IntegerField(primary_key=True)
    nombres = models.CharField(max_length=30,null=False)
    apellidos = models.CharField(max_length=30,null=False)
    idname = models.IntegerField(null=False)
    numcon = models.IntegerField(null=False)
    cargo = models.CharField(max_length=30,null=False)
    telefono = models.IntegerField(null=False)
    
    class Meta:
        db_table = 'usuarios'
