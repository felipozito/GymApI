
from django.urls import path
from .views import UserViews, UserViewsDetail

urlpatterns = [
    path('users/', UserViews, name="Users API"),
    path('users/<int:pk>', UserViewsDetail, name="Users API Detail")
]