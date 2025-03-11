
from django.urls import path
from Apps.bases.views import PruebaView, PruebaDetailView, RutinesView

urlpatterns = [
   path('', PruebaView, name='pruebaAPI'),
   path('<int:id>/', PruebaDetailView, name='pruebaDetailAPI'),
   path('rutines/', RutinesView, name='rutineDetailAPI'),
]