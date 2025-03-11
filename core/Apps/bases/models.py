from django.db import models

# Create your models here.
class User(models.Model):
    ROL_CHOICES = (
        ('ADMIN', 'ADMIN'),
        ('PM', 'PM'),
        ('CONTABILIDAD', 'CONTABILIDAD'),
    )
    id= models.AutoField(primary_key=True,unique=True) 
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.CharField(max_length=100, unique=True)
    telefono = models.CharField(max_length=100)
    fecha_nacimiento = models.DateField()
    rol= models.CharField(max_length=100, choices=ROL_CHOICES)
    
    
    def __str__(self):
        return self.nombre
    
class Rutine(models.Model):
    id= models.AutoField(primary_key=True,unique=True) 
    nombre = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=100)
    fecha_creacion = models.DateField( auto_now=True)
    user_id = models.ForeignKey(User, related_name='routines', on_delete=models.CASCADE,)
    
    def __str__(self):
        return self.nombre
    