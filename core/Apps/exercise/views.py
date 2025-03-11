from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Exercise
from .serializers import ExerciseSerializer
from rest_framework import status

@api_view(['GET', 'POST'])
def ExercisesListView(request):
    if request.method == 'GET':
        exercises = Exercise.objects.all()
        serializer = ExerciseSerializer(exercises, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = ExerciseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET', 'PATCH', 'DELETE'])
def ExcersiceDetailView(request, id):
    try:
        exercise = Exercise.objects.get(id=id)
    except Exercise.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = ExerciseSerializer(exercise)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    elif request.method == 'PATCH':
        serializer = ExerciseSerializer(exercise, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        exercise.delete()
        return Response({"Messages":"Ejercicio Borrado"},status=status.HTTP_204_NO_CONTENT)