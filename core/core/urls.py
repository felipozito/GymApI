
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/prueba/', include('Apps.bases.urls')),  # Updated path for bases app
    path('api/v1/', include('Apps.user.urls')),
    path('api/v1/', include('Apps.exercise.urls')),
    path('api/v1/', include('Apps.memberships.urls')),
]
