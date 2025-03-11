from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .models import User  # Asegúrate de que el modelo se llame User
from .serializers import UserSerializer  # Asegúrate de que el serializador se llame UserSerializer

@api_view(['GET','POST'])
def UserViews(request):
    if request.method=='GET':
        users=User.objects.all()
        serializers=UserSerializer(users,many=True)
        return Response(serializers.data , status=status.HTTP_200_OK)
    if request.method=='POST':
        serializers = UserSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response({"messages":"Error datos"}, status=status.HTTP_400_NOT_FOUND)

@api_view(['GET','PATCH','DELETE'])
def UserViewsDetail(request,pk):
    try:
        users=User.objects.get(pk=pk)
    except User.DoesNotExist:
        return Response({"messages":"No existe"}, status=status.HTTP_404_NOT_FOUND)
    if request.method=='GET':
        serializers=UserSerializer(users)
        return Response(serializers.data , status=status.HTTP_200_OK)
    if request.method=='PATCH':
        serializers = UserSerializer(users,data=request.data,partial=True)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response({"messages":"Error datos"}, status=status.HTTP_400_NOT_FOUND)
    if request.method=='DELETE':
        users.delete()
        return Response({"messages":"Eliminado"}, status=status.HTTP_204_NO_CONTENT)