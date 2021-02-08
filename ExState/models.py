from django.db import models
import uuid
from django.utils import timezone
# Create your models here.
'''タスク実行状況DB'''
class ExState(models.Model):
    class Meta:
        db_table = 'ExState'
    id = models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False) #管理番号
    departmentID = models.CharField(verbose_name='部門コード',max_length=5) #部門マスターキー
    taskID = models.CharField(verbose_name='タスクコード',max_length=5) #タスクマスターキー
    TargetMonth = models.CharField(verbose_name='対象年月',max_length=6) #対象年月YYYYMM レコード作成の際にDateFieldからYYYYMMを取得
    toDoFlg = models.BooleanField(verbose_name='実行状況',default=False)
    
    def __str__(self):
        return self.id
    