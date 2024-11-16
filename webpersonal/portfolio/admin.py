from django.contrib import admin
from .models import Project
# Register your models here.
#para que podamos modificar la fecha de entrega
class ProjectAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

#para registrar los proyectos y que los podamos guardar    
admin.site.register(Project)