from django.contrib import admin
from .models import Membership, UserMembership
# Register your models here.
@admin.register(Membership)
class MembershipAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'price',)
    list_display_links = ('id', 'nombre')
    
@admin.register(UserMembership)
class UserMembershipAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'membership', 'discount', 'start_date', 'end_date',  'status')
    list_display_links = ('id', 'user')
    