from rest_framework import serializers
from .models import User, Rutine
"""
UN serializer es una clase que se encarga de convertir los datos de un modelo a un formato que se pueda enviar a través de la red,
por ejemplo, a través de una API REST. 
"""
class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['nombre', 'apellido', 'email', 'telefono', 'fecha_nacimiento', 'rol']
    
    def validate_telefono(self, value):
        # Verifica que el teléfono tenga exactamente 10 dígitos
        if not value.isdigit() or len(value) != 10:
            raise serializers.ValidationError("El teléfono debe tener exactamente 10 dígitos.")
        return value

class UserDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['nombre', 'apellido', 'email', 'telefono', 'fecha_nacimiento']


class RutineSerializer(serializers.ModelSerializer):
    user_details = UsersSerializer(source='user_id', read_only=True) 
    class Meta:
        model = Rutine
        fields = ['nombre', 'descripcion', 'fecha_creacion', 'user_id', 'user_details']
    
"""
Igualmente se puede hacer de la siguiente manera
class ListSerializer(serializers.Serializer):
    nombre = serializers.CharField()
    apellido = serializers.CharField()
    
class ListSerializer(serializers.ModelSerializer):
    class Meta:
        model = prueba
        fields = '__all__'
"""
        

