from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .models import User,Rutine
from .serializer import UsersSerializer, UserDetailSerializer, RutineSerializer

"""class PruebaViewSet(APIView):
    def get(self, request):
        queryset = prueba.objects.all()
        serializer=ListSerializer(queryset, many=True)
        return Response(serializer.data)
"""

@api_view(['GET', 'POST', ])
def PruebaView(request):
    if request.method == 'GET':
        queryset = User.objects.all()
        serializer = UsersSerializer(queryset, many=True)
        response={
            'messages':'Lista de Usuarios',
            'data': serializer.data
        }
        #return Response(serializer.data , status=status.HTTP_200_OK)
        return Response(response, status=status.HTTP_202_ACCEPTED)
    if request.method == 'POST':
        serializer = UsersSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response( serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET', 'PATCH', 'DELETE'])
def PruebaDetailView(request, id):
    queryset = User.objects.filter(id=id).first()
    if queryset:
        if request.method == 'GET':
            serializer = UserDetailSerializer(queryset)
            return Response(serializer.data, status=status.HTTP_200_OK)
        
        if request.method == 'DELETE':
            queryset.delete()
            return Response({"messages":"Usuario Eliminado"},status=status.HTTP_200_OK)
        
        if request.method == 'PATCH':
            serializer = UserDetailSerializer(queryset, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response({'messages':'Usuario Editado correctamente'} ,status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    return Response({'messages':'No existe un usuario con ese parametro'}, serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    
@api_view(['GET','POST'])
def RutinesView(request):
    if request.method == 'POST':
        serializer = RutineSerializer(data=request.data)
        print(request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    if request.method == 'GET':
        rutines = Rutine.objects.all()
        if rutines:
            serializer = RutineSerializer(rutines, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response({'messages':'No hay rutinas'}, status=status.HTTP_400_BAD_REQUEST)

    
    

