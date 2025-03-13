from rest_framework import serializers
from .models import Membership, UserMembership
from django.utils import timezone
from datetime import timedelta
from Apps.user.models import User

# Serializador general para Modelo Memberships
class MembershipSerializer(serializers.ModelSerializer):
    class Meta:
        model = Membership
        fields = '__all__'
# Serializador general para Modelo UserMemberships
class UserMembershipSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserMembership
        fields = '__all__'
        
class UserMembershipDetailSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    membership = serializers.PrimaryKeyRelatedField(queryset=Membership.objects.all())
    # *Funcion para la creacion de la fecha de expiracion según el tipo de membresía
    def create(self, validated_data):
           # Obtener la fecha de inicio o usar la fecha actual si no se proporciona
        start_date = validated_data.get('start_date', timezone.now().date())
        if hasattr(start_date, 'date'):  # Convertir a date si es necesario
            start_date = start_date.date()
        # Obtener el tipo de membresía y su ID
        membership = validated_data.get('membership')
        membership_id = membership.id if membership else 1
        # Definir la duración de la membresía según su tipo
        membership_durations = {
            1: timedelta(days=30),   # Membresía tipo 1: 30 días
            2: timedelta(days=90),   # Membresía tipo 2: 90 días
            3: timedelta(days=365),  # Membresía tipo 3: 365 días (1 año)
        }
        # Calcular la fecha de finalización usando la duración correspondiente
        duration = membership_durations.get(membership_id, timedelta(days=30))  # Valor predeterminado: 30 días
        validated_data['end_date'] = start_date + duration
        # Crear y retornar la instancia de UserMembership
        return UserMembership.objects.create(**validated_data)
    class Meta: # Definir el modelo y los campos a serializar
        model = UserMembership
        fields = '__all__'
        

    