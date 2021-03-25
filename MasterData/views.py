from django.shortcuts import render
from django_filters import rest_framework as filters
from rest_framework import status, generics,views
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response
from .models import TasksMaster,DeptsMaster
from .serializers import DeptsSerializer,TasksSerializer
from django.shortcuts import get_object_or_404

# Create your views here.
class GetDeptsMaster(generics.ListAPIView):
    """部署マスターから一覧を取得する(ExStateでの同名と同様)"""
    queryset = DeptsMaster.objects.all()
    serializer_class = DeptsSerializer
    filter_backends = [filters.DjangoFilterBackend]
    filterset_fields = '__all__'

class GetTasksMaster(generics.ListAPIView):
    """タスクマスターから一覧を取得する(ExStateでの同名と同様)"""
    queryset = TasksMaster.objects.all()
    serializer_class = TasksSerializer
    filter_backends = [filters.DjangoFilterBackend]
    filterset_fields = '__all__'

class GetDeptsRetriveAPIView(generics.RetrieveAPIView):
    queryset = DeptsMaster.objects.all()
    serializer_class = DeptsSerializer
    lookup_fields = '__all__'

class GetTasksRetriveAPIView(generics.RetrieveAPIView):
    queryset = TasksMaster.objects.all()
    serializer_class = TasksSerializer
    lookup_fields = '__all__'
