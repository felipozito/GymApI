from django.db import models

# Create your models here.
class User(models.Model):
    ROLES = (
        ('Admin', 'admin'),
        ('Member', 'Member'),
        ('Trainer', 'Trainer')
    )
    id=models.AutoField(primary_key=True, unique=True)  
    name = models.CharField(max_length=50)
    lastname=models.CharField(max_length=50, default='')
    age=models.IntegerField(blank=True, null=True)
    height=models.FloatField(blank=True, null=True)
    weight=models.FloatField(blank=True, null=True)
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    role = models.CharField(max_length=50, choices=ROLES, default='Member')
    def __str__(self):
        return self.name

