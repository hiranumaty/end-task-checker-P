from rest_framework import serializers
from .models import DeptsMaster,TasksMaster

class DeptsSerializer(serializers.ModelSerializer):
    class Meta:
        model = DeptsMaster
        fields = ['id','deploy_name','created_at']

class TasksSerializer(serializers.ModelSerializer):
    class Meta:
        model = TasksMaster
        fields = ['id','Task_name','created_at']