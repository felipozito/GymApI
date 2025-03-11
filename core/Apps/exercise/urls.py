
from django.urls import path
from .views import ExercisesListView,ExcersiceDetailView

urlpatterns = [
    path('exercises', ExercisesListView, name='Lista De Ejercicios'),
    path('exercises/<int:id>/', ExcersiceDetailView, name='Detalle De Ejercicio'),
]
