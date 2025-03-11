from django.contrib import admin
from .models import Exercise
# Register your models here.
@admin.register(Exercise)
class ExerciseAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'difficulty', 'muscle_group', 'equipment', 'created_at', 'updated_at')
    list_display_links = ('id', 'name')
    list_filter = ('muscle_group', 'difficulty')
    search_fields = ('name', 'muscle_group', 'difficulty')
    ordering = ('name', 'muscle_group')
    readonly_fields = ('created_at', 'updated_at')
  
    """ TODO def get_readonly_fields(self, request, obj=None):
        if request.user.groups.filter(name='Administrador').exists():
            return ('created_at', 'updated_at')
        else:
            return ('name', 'description', 'difficulty', 'muscle_group', 'equipment', 'created_at', 'updated_at')
    def has_add_permission(self, request):
        return request.user.groups.filter(name='Administrador').exists()
    def has_change_permission(self, request, obj=None):
        return request.user.groups.filter(name='Administrador').exists()
    def has_delete_permission(self, request, obj=None):
        return request.user.groups.filter(name='Administrador').exists()
    def has_view_permission(self, request, obj=None):
        return request.user.groups.filter(name='Administrador').exists()
    def has_module_permission(self, request):
        return request.user.groups.filter(name='Administrador').exists()"""