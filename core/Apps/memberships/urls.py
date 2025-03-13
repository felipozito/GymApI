from django.urls import path
from .views import MembershipslistView, MembershipDetailView, UserMembershipListView, UserMembershipDetailView,CreateUserMembershipView, ActiveUserMembershipView
#ActiveUserMembershipView

urlpatterns = [
    #Gestion de mebresias totales
    path('memberships/', MembershipslistView, name="Memberships API"),
    path('memberships/<int:pk>/', MembershipDetailView, name="Memberships API Detail"),
    #Gestion de membresias de usuarios
    path('memberships/user/<int:id>/', UserMembershipListView, name="User Memberships API"),
    path('memberships/user/<int:user_id>/membership/<int:membership_id>/', UserMembershipDetailView, name="User Membership Detail"),
    path('memberships/user/<int:user_id>/active/', ActiveUserMembershipView, name="User Active Membership"),
    #URLs para operaciones específicas de membresías (ejemplos adicionales)
    path('memberships/create/<int:user_id>/<int:membership_type_id>/', CreateUserMembershipView, name="create_user_membership"),
    
    
]