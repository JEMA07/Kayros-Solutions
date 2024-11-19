from django.contrib import admin
from .models import Projects, Task


#crer una clases para solo pueda mostrar la fecha 
class taskadmin(admin.ModelAdmin):
    readonly_fields=("created",)
    
    
#registra las clases al admin
admin.site.register(Projects)
admin.site.register(Task, taskadmin)
