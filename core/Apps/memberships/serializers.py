from rest_framework import serializers
from .models import Membership, UserMembership
from django.utils import timezone
from datetime import timedelta

# !Serializador general para Modelo Memberships
class MembershipSerializer(serializers.ModelSerializer):
    class Meta:
        model = Membership
        fields = '__all__'
#!Serializador general para Modelo UserMemberships
class UserMembershipSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserMembership
        fields = '__all__'
#TODO Serializador para UserMemberships para la obtencion detallada de 1
class UserMembershipDetailSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()
    membership = serializers.StringRelatedField()
    
    # *Funcion para la creacion de la fecha de expiracion
    def create(self, validated_data):
        # Calculate end_date (30 days from start_date)
        start_date = validated_data.get('start_date', timezone.now())
        validated_data['end_date'] = start_date + timedelta(days=30)
        # Create the instance with the calculated end_date
        return super().create(validated_data)
    
    def to_representation(self, instance):
        # Only return active memberships
        if instance.status:  # status is a BooleanField where True means active
            return super().to_representation(instance)
        return None
    class Meta:
        model = UserMembership
        fields = '__all__'
        

    