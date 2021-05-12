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

class DeptsFilter(filters.FilterSet):
    class Meta:
        model = DeptsMaster
        fields = '__all__'
class GetDeptsRetriveAPIView(generics.RetrieveAPIView):
    queryset = DeptsMaster.objects.all()
    serializer_class = DeptsSerializer
    lookup_fields = '__all__'

class ChangeDeptsAPIView(generics.RetrieveUpdateAPIView):
    queryset = DeptsMaster.objects.all()
    serializer_class = DeptsSerializer
    lookup_fields = '__all__'

class CheckDeptsValidAPIView(views.APIView):
    def post(self,request,TargetDay,*args,**kwargs):
        '''
        指定した日付のデータを取得して、有効フラグをonにする
        '''
        UpdateData = []
        Dept_filterset = DeptsFilter(request.query_params,queryset=DeptsMaster.objects.filter(valid_flg=False,valid_start=TargetDay))
        Dept_serializer = DeptsSerializer(instance=Dept_filterset.qs,many=True)
        DeptDatas = Dept_serializer.data
        for DeptData in DeptDatas:
            Dept_instance = DeptsMaster(**DeptData)
            Dept_instance.valid_flg = True
            UpdateData.append(Dept_instance)
        DeptsMaster.objects.bulk_update(UpdateData,fields=['valid_flg'])
        return Response('',status.HTTP_200_OK)

class CreateDeptsAPIView(views.APIView):

    def post(self,request,*args,**kwargs):
        serializer = DeptsSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status.HTTP_201_CREATED)

class TaskFilter(filters.FilterSet):
    class Meta:
        model = TasksMaster
        fields = '__all__'
 
class GetTasksRetriveAPIView(generics.RetrieveAPIView):
    queryset = TasksMaster.objects.all()
    serializer_class = TasksSerializer
    lookup_fields = '__all__'

class ChangeTasksAPIView(generics.RetrieveUpdateAPIView):
    queryset = TasksMaster.objects.all()
    serializer_class = TasksSerializer
    lookup_fields = '__all__'

class CheckTasksValidAPIView(views.APIView):
    def post(self,request,TargetDay,*args,**kwargs):
        '''
        指定した日付のデータを取得して、有効フラグをonにする
        '''
        UpdateData = []
        Tasks_filterset = TaskFilter(request.query_params,queryset=TasksMaster.objects.filter(valid_flg=False,valid_start=TargetDay))
        Tasks_serializer = TasksSerializer(instance=Tasks_filterset.qs,many=True)
        TaskDatas = Tasks_serializer.data
        for TaskData in TaskDatas:
            Task_instance = TasksMaster(**TaskData)
            Task_instance.valid_flg = True
            UpdateData.append(Task_instance)
        TasksMaster.objects.bulk_update(UpdateData,fields=['valid_flg'])
        return Response('',status.HTTP_200_OK)

class CreateTasksAPIView(views.APIView):

    def post(self,request,*args,**kwargs):
        serializer = TasksSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status.HTTP_201_CREATED)
