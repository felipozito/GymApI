from django.urls import path
from .views import MembershipslistView, MembershipDetailView, UserMembershipListView, UserMembershipDetailView, ActiveUserMembershipView
from .example_views import CreateUserMembershipView, RenewUserMembershipView, CancelUserMembershipView, MembershipStatsView

# Ejemplo de configuración de URLs para las vistas de membresías
urlpatterns = [
    # URLs básicas para gestión de tipos de membresías
    path('memberships/', MembershipslistView, name="memberships_list"),
    path('memberships/<int:pk>/', MembershipDetailView, name="membership_detail"),
    
    # URLs para gestión de membresías de usuarios
    path('memberships/user/<int:id>/', UserMembershipListView, name="user_memberships_list"),
    path('memberships/user/<int:user_id>/membership/<int:membership_id>/', UserMembershipDetailView, name="user_membership_detail"),
    path('memberships/user/<int:user_id>/active/', ActiveUserMembershipView, name="user_active_membership"),
    
    # URLs para operaciones específicas de membresías (ejemplos adicionales)
    path('memberships/create/<int:user_id>/<int:membership_type_id>/', CreateUserMembershipView, name="create_user_membership"),
    path('memberships/renew/<int:user_id>/', RenewUserMembershipView, name="renew_user_membership"),
    path('memberships/cancel/<int:user_id>/', CancelUserMembershipView, name="cancel_user_membership"),
    path('memberships/stats/', MembershipStatsView, name="membership_stats"),
]

# Ejemplo de cómo usar estas URLs en tu aplicación:
"""
Ejemplos de uso:

1. Obtener todos los tipos de membresías disponibles:
   GET /api/memberships/

2. Obtener detalles de un tipo de membresía específico:
   GET /api/memberships/1/

3. Obtener todas las membresías de un usuario:
   GET /api/memberships/user/1/

4. Obtener detalles de una membresía específica de un usuario:
   GET /api/memberships/user/1/membership/2/

5. Obtener la membresía activa de un usuario:
   GET /api/memberships/user/1/active/

6. Crear una nueva membresía para un usuario:
   POST /api/memberships/create/1/2/
   Body: {"discount": 10.0}

7. Renovar la membresía de un usuario:
   POST /api/memberships/renew/1/

8. Cancelar la membresía activa de un usuario:
   PATCH /api/memberships/cancel/1/

9. Obtener estadísticas de membresías:
   GET /api/memberships/stats/
"""