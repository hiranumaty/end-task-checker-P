from rest_framework import serializers
from .models import ExState

class ExStateSerializer(serializers.ModelSerializer):
    """タスク消化状況モデルのシリアライザ"""
    class Meta:
        model = ExState
        fields = ['deploy_name','Task_name','TargetMonth','toDoFlg']
    
    #結合しているマスターテーブルから部門名とタスク名を取得する
    deploy_name = serializers.CharField(source='depart.deploy_name')
    Task_name = serializers.CharField(source='task.Task_name')

class ExStateListSerializer(serializers.ListSerializer):
    """タスク消化状況モデルのリストシリアライザ"""
    child = ExStateSerializer()