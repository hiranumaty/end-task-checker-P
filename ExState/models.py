from django.db import models
import uuid
from django.utils import timezone
from MasterData.models import TasksMaster, DeptsMaster
# Create your models here.
'''タスク実行状況DB'''


class ExState(models.Model):
    class Meta:
        db_table = 'ExState'
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False)  # 管理番号
    # 対象年月YYYYMM レコード作成の際にDateFieldからYYYYMMを取得
    TargetMonth = models.CharField(verbose_name='対象年月', max_length=6)
    toDoFlg = models.BooleanField(verbose_name='実行状況', default=False)

    # ここでリレーションの関係を記載 どうやらOne to Manyらしい
    task = models.ForeignKey(
        TasksMaster,
        verbose_name='タスク名',
        on_delete=models.SET_NULL,
        null=True)
    depart = models.ForeignKey(
        DeptsMaster,
        verbose_name='部署',
        on_delete=models.SET_NULL,
        null=True)
