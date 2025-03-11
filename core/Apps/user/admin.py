from django.contrib import admin
from .models import User
# Register your models here.

@admin.register(User)

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('id','name','lastname','age','height','weight','email','password','role' )  # Campos que se mostrarán en la lista
    list_display_links = ('id','name','lastname','email')  # Campos que serán enlaces para acceder al detalle
    search_fields = ('name','lastname','email')


