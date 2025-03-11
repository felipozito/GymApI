from django.contrib import admin
from .models import User, Rutine
# Register your models here.
@admin.register(User)
class pruebaAdmin(admin.ModelAdmin):
    list_display = ('id','nombre', 'apellido', 'email', 'telefono', 'fecha_nacimiento', 'rol')  # Removed space after 'apellido'
    search_fields = ['apellido', 'email']
    list_filter = ['rol']

@admin.register(Rutine)
class rutineAdmin(admin.ModelAdmin):
    list_display = ('id','nombre','user_id', 'descripcion', 'fecha_creacion')  # Removed space after 'apellido'
    search_fields = ['nombre', 'user_id']
    list_filter = ['fecha_creacion']