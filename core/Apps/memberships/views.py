from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Membership, UserMembership  
from Apps.user.models import User
from .serializers import MembershipSerializer, UserMembershipSerializer

# Create your views here.

@api_view(['GET', 'POST'])
def MembershipslistView(request):
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
def MembershipDetailView(request, pk):
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
def UserMembershipListView(request,id):
    try:
        user = User.objects.get(id=id)
    except User.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        user_membership = UserMembership.objects.filter(user=user)
        serializer = UserMembershipSerializer(user_membership, many=True)
        return Response(serializer.data)
    
#TODO Realizar membresia activa   
@api_view(['GET', 'POST', 'PATCH', 'DELETE'])
def UserMembershipDetailView(request, user_id, membership_id):
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
