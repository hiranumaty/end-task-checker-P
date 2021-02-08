from django.db import models
from django.utils import timezone
"""タスクマスター及び部門のマスターを含む"""
# Create your models here.

class TasksMaster(models.Model):
    class Meta:
        db_table = 'Tasks'
    id = models.CharField(primary_key=True,max_length=5,verbose_name='タスクコード')
    Task_name = models.CharField(verbose_name='タスク名',max_length=30)
    created_at = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return self.Task_name
    

class DeptsMaster(models.Model):
    class Meta:
        db_table = 'Depts'
    id = models.CharField(primary_key=True,max_length=5,verbose_name='所属コード')
    deploy_name = models.CharField(verbose_name='部署名',max_length=30)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.deploy_name