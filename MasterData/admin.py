from django.contrib import admin
from .models import DeptsMaster,TasksMaster

class TaskModelAdmin(admin.ModelAdmin):
    list_display = ('id','Task_name','created_at')
    ordering=('id',)
    #readonly_fields = ('id','Task_name','created_at')

class DeptsModelAdmin(admin.ModelAdmin):
    list_display = ('id','deploy_name','created_at')
    ordering=('id',)
    #readonly_fields = ('id','deploy_name','created_at')

# Register your models here.
admin.site.register(TasksMaster,TaskModelAdmin)
admin.site.register(DeptsMaster,DeptsModelAdmin)

