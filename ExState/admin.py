from django.contrib import admin
from .models import ExState

# Register your models here.


class ExStateAdmin(admin.ModelAdmin):
    list_display = ('id', 'TargetMonth', 'depart', 'task', 'toDoFlg')
    list_filter = ('TargetMonth',)
    # readonly_fields = ('id','depart','task',)
    # search_fields = ['',]
    ordering = ('TargetMonth', 'depart',)


admin.site.register(ExState, ExStateAdmin)
