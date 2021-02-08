from django.contrib import admin
from .models import ExState

# Register your models here.
class ExStateAdmin(admin.ModelAdmin):
    list_display = ('departmentID','taskID','TargetMonth','toDoFlg')
    list_filter = ('TargetMonth','departmentID',)
    readonly_fields = ('departmentID','taskID',)
    search_fields = ['departmentID',]
    ordering = ('-TargetMonth','-departmentID',)
admin.site.register(ExState,ExStateAdmin)