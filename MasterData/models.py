from django.db import models
from django.utils import timezone
"""タスクマスター及び部門のマスターを含む"""
# Create your models here.

class DeptsMaster(models.Model):
    class Meta:
        db_table = 'Depts'
    id = models.CharField(primary_key=True, max_length=5, verbose_name='所属コード')
    deploy_name = models.CharField(verbose_name='部署名', max_length=30)
    valid_flg = models.BooleanField(verbose_name='有効フラグ',default=True)
    valid_start = models.DateField()
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.deploy_name

class TasksMaster(models.Model):
    class Meta:
        db_table = 'Tasks'
    id = models.CharField(
        primary_key=True,
        max_length=5,
        verbose_name='タスクコード')
    Task_name = models.CharField(verbose_name='タスク名', max_length=30)
    valid_flg = models.BooleanField(verbose_name='有効フラグ',default=True)
    valid_start = models.DateField(verbose_name='有効開始日')
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.Task_name


