from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Membership, UserMembership
from Apps.user.models import User
from .serializers import MembershipSerializer, UserMembershipSerializer, UserMembershipDetailSerializer
from django.utils import timezone
from datetime import timedelta


# Ejemplo de vista para crear una nueva membresía de usuario
@api_view(['POST'])
def CreateUserMembershipView(request, user_id, membership_type_id):
    try:
        user = User.objects.get(id=user_id)
        membership_type = Membership.objects.get(id=membership_type_id)
    except User.DoesNotExist:
        return Response({"message": "Usuario no encontrado"}, status=status.HTTP_404_NOT_FOUND)
    except Membership.DoesNotExist:
        return Response({"message": "Tipo de membresía no encontrado"}, status=status.HTTP_404_NOT_FOUND)
    
    # Verificar si el usuario ya tiene una membresía activa
    active_membership = UserMembership.objects.filter(user=user, status=True).first()
    if active_membership:
        return Response({"message": "El usuario ya tiene una membresía activa"}, status=status.HTTP_400_BAD_REQUEST)
    
    # Preparar los datos para la nueva membresía
    data = {
        'user': user.id,
        'membership': membership_type.id,
        'discount': request.data.get('discount', 0.0),
        'start_date': request.data.get('start_date', timezone.now().date()),
        'status': True
    }
    
    serializer = UserMembershipDetailSerializer(data=data)
    if serializer.is_valid():
        # El método create del serializer calculará automáticamente end_date
        user_membership = serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Ejemplo de vista para renovar una membresía
@api_view(['POST'])
def RenewUserMembershipView(request, user_id):
    """
    Vista para renovar la membresía de un usuario por 30 días más.
    """
    try:
        user = User.objects.get(id=user_id)
        membership = UserMembership.objects.get(user=user)
    except User.DoesNotExist:
        return Response({"message": "Usuario no encontrado"}, status=status.HTTP_404_NOT_FOUND)
    except UserMembership.DoesNotExist:
        return Response({"message": "El usuario no tiene membresía"}, status=status.HTTP_404_NOT_FOUND)
    
    # Renovar la membresía por 30 días más desde la fecha actual
    membership.start_date = timezone.now().date()
    membership.end_date = membership.start_date + timedelta(days=30)
    membership.status = True  # Asegurar que esté activa
    membership.save()
    
    serializer = UserMembershipDetailSerializer(membership)
    return Response(serializer.data, status=status.HTTP_200_OK)


# Ejemplo de vista para cancelar una membresía
@api_view(['PATCH'])
def CancelUserMembershipView(request, user_id):
    """
    Vista para cancelar la membresía activa de un usuario.
    """
    try:
        user = User.objects.get(id=user_id)
        membership = UserMembership.objects.get(user=user, status=True)
    except User.DoesNotExist:
        return Response({"message": "Usuario no encontrado"}, status=status.HTTP_404_NOT_FOUND)
    except UserMembership.DoesNotExist:
        return Response({"message": "El usuario no tiene membresía activa"}, status=status.HTTP_404_NOT_FOUND)
    
    # Desactivar la membresía
    membership.status = False
    membership.save()
    
    return Response({"message": "Membresía cancelada correctamente"}, status=status.HTTP_200_OK)


# Ejemplo de vista para obtener estadísticas de membresías
@api_view(['GET'])
def MembershipStatsView(request):
    """
    Vista para obtener estadísticas de membresías.
    """
    total_memberships = UserMembership.objects.count()
    active_memberships = UserMembership.objects.filter(status=True).count()
    inactive_memberships = total_memberships - active_memberships
    
    # Contar membresías por tipo
    membership_types = Membership.objects.all()
    memberships_by_type = {}
    
    for membership_type in membership_types:
        count = UserMembership.objects.filter(membership=membership_type).count()
        memberships_by_type[membership_type.nombre] = count
    
    stats = {
        "total_memberships": total_memberships,
        "active_memberships": active_memberships,
        "inactive_memberships": inactive_memberships,
        "memberships_by_type": memberships_by_type
    }
    
    return Response(stats, status=status.HTTP_200_OK)