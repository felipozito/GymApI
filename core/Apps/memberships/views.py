from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.utils import timezone
from .models import Membership, UserMembership  
from Apps.user.models import User
from .serializers import MembershipSerializer, UserMembershipSerializer, UserMembershipDetailSerializer

# Create your views here.

@api_view(['GET', 'POST']) 
def MembershipslistView(request): #*Vista para listar y crear membresias
    if request.method == 'GET':
        memberships = Membership.objects.all()
        serializer = MembershipSerializer(memberships, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = MembershipSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PATCH', 'DELETE'])
def MembershipDetailView(request, pk): #*Vista para detalle, actualizacion y eliminacion de membresias GENERAL
    try:
        membership = Membership.objects.get(pk=pk)
    except Membership.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = MembershipSerializer(membership)
        return Response(serializer.data)

    elif request.method == 'PATCH':
        serializer = MembershipSerializer(membership, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        membership.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
@api_view(['GET'])
def UserMembershipListView(request,id): #*Vista para listar y crear membresias de un usuario
    try:
        user = User.objects.get(id=id)
    except User.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        user_membership = UserMembership.objects.filter(user=user)
        serializer = UserMembershipSerializer(user_membership, many=True)
        return Response(serializer.data)

@api_view(['GET', 'POST', 'PATCH', 'DELETE'])
def UserMembershipDetailView(request, user_id, membership_id): #*Vista para detalle, actualizacion y eliminacion de membresias de un usuario
    try:
        user = User.objects.get(id=user_id)
        membership = UserMembership.objects.get(id=membership_id, user=user)
    except User.DoesNotExist:
        return Response({"message": "Usuario no existe"}, status=status.HTTP_404_NOT_FOUND)
    except UserMembership.DoesNotExist:
        return Response({"message": "Membresía no existe"}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = UserMembershipSerializer(membership)
        return Response(serializer.data)
    if request.method == 'PATCH':
        serializer = UserMembershipSerializer(membership, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    if request.method == 'DELETE':
        membership.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
@api_view(['GET'])
def ActiveUserMembershipView(request, user_id): #*Vista para listar membresias de un usuario ACTIVA
    try:
        user = User.objects.get(id=user_id)
    except User.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        active_membership = UserMembership.objects.filter(user=user, status=True).first()
        if active_membership:
            serializer = UserMembershipSerializer(active_membership)
            return Response(serializer.data)
        return Response({"message": "No se encontró una membresía activa para el usuario"}, status=status.HTTP_404_NOT_FOUND)

@api_view(['POST'])
def CreateUserMembershipView(request, user_id, membership_type_id):
    try:
        user = User.objects.get(id=user_id)
        membership_type = Membership.objects.get(id=membership_type_id)
    except User.DoesNotExist:
        return Response({"message": "Usuario no encontrado"}, status=status.HTTP_404_NOT_FOUND)
    except Membership.DoesNotExist:
        return Response({"message": "Tipo de membresía no encontrado"}, status=status.HTTP_404_NOT_FOUND)
    
    # Verificar si el usuario ya tiene una membresía activa y desactivarla
    active_memberships = UserMembership.objects.filter(user=user, status=True)
    if active_memberships.exists():
        # Desactivar todas las membresías activas existentes
        active_memberships.update(status=False)
    
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
