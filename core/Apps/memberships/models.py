from django.db import models
from Apps.user.models import User

# Create your models here.

class Membership(models.Model):
    id=models.AutoField(primary_key=True, unique=True)
    nombre = models.CharField(max_length=30)
    price = models.FloatField(default=20.00)
    
    def __str__(self):
        return self.nombre
    
class UserMembership(models.Model):
    STATUS=(
        ('active', 'Active'),
        ('inactive', 'Inactive'),
    )
    id=models.AutoField(primary_key=True, unique=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    membership = models.ForeignKey(Membership, on_delete=models.SET_NULL, null=True)
    discount= models.FloatField(default=0.0)
    start_date = models.DateField(auto_now=True, blank=True)
    end_date = models.DateField(null=True)
    status= models.BooleanField(default=True)   
    def __str__(self):
        return self.user.name
    