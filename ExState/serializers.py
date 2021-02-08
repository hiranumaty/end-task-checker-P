from rest_framework import serializers
from .models import ExState

class ExStateSerializer(serializers.ModelSerializer):
    """実行済みタスク用のシリアライザ"""
    class Meta:
        model = ExState
        fields = ['departmentID','taskID','TargetMonth','toDoFlg']