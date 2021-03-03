from rest_framework import serializers
from .models import ExState


class ExStateSerializer(serializers.ModelSerializer):
    """
    タスク消化状況モデルのシリアライザ
    結合しているマスターテーブルから部門名とタスク名を取得する
    """
    class Meta:
        model = ExState
        fields = [
            'id',
            'deploy_id',
            'deploy_name',
            'Task_id',
            'Task_name',
            'TargetMonth',
            'toDoFlg']

    deploy_id = serializers.CharField(source='depart.id')
    deploy_name = serializers.CharField(source='depart.deploy_name')
    Task_id = serializers.CharField(source='task.id')
    Task_name = serializers.CharField(source='task.Task_name')
    order_by = ['TargetMonth','deploy_id','Task_id']


class ExStateListSerializer(serializers.ListSerializer):
    """タスク消化状況モデルのリストシリアライザ"""
    child = ExStateSerializer()
