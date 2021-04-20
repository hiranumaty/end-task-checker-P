from django_filters import rest_framework as filters
from rest_framework import status, generics,views
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response
from .models import ExState
from .serializers import ExStateSerializer
from MasterData.models import TasksMaster,DeptsMaster
from MasterData.serializers import DeptsSerializer,TasksSerializer
from django.shortcuts import get_object_or_404


class MultipleFieldLookupMixin(object):
    """
    複数検索をサポートするクラス (これを継承することで、複数キーの検索をサポート)
    Apply this mixin to any view or viewset to get multiple field filtering
    based on a `lookup_fields` attribute, instead of the default single field filtering.
    """

    def get_object(self):
        queryset = self.get_queryset()             # Get the base queryset
        queryset = self.filter_queryset(queryset)  # Apply any filter backends
        filter = {}
        for field in self.lookup_fields:
            if self.kwargs[field]:  # Ignore empty fields.
                filter[field] = self.kwargs[field]
        obj = get_object_or_404(queryset, **filter)  # Lookup the object
        self.check_object_permissions(self.request, obj)
        return obj


class ExStateFilter(filters.FilterSet):
    class Meta:
        model = ExState
        fields = '__all__'

class DeptsFilter(filters.FilterSet):
    class Meta:
        model = DeptsMaster
        fields = '__all__'

class TasksFilter(filters.FilterSet):
    class Meta:
        model = TasksMaster
        fields = '__all__'

class GetDeptsMaster(generics.ListAPIView):
    """部署マスターから一覧を取得する"""
    queryset = DeptsMaster.objects.all()
    serializer_class = DeptsSerializer
    filter_backends = [filters.DjangoFilterBackend]
    filterset_fields = '__all__'

class GetTasksMaster(generics.ListAPIView):
    """タスクマスターから一覧を取得する"""
    queryset = TasksMaster.objects.all()
    serializer_class = TasksSerializer
    filter_backends = [filters.DjangoFilterBackend]
    filterset_fields = '__all__'

class ExStateListAPIView(generics.ListAPIView):
    """一覧の総取得"""
    queryset = ExState.objects.all()
    serializer_class = ExStateSerializer
    filter_backends = [filters.DjangoFilterBackend]
    filterset_fields = '__all__'


class ExStateListMonthAPIView(views.APIView):
    """月を指定して取得する"""
    def get(self,request,TargetMonth,*args,**kwargs):
        filterset = ExStateFilter(request.query_params,queryset=ExState.objects.filter(TargetMonth=TargetMonth).order_by('depart_id','task_id'))
        if not filterset.is_valid():
            raise ValidationError(filterset.errors)
        serializer = ExStateSerializer(instance=filterset.qs,many=True)
        return Response(serializer.data,status.HTTP_200_OK)

class ExStateListDeptMonthAPIView(views.APIView):
    """月と部署を選択して取得する"""
    def get(self,request,TargetMonth,depart_id,*args,**kwargs):
        filterset = ExStateFilter(request.query_params,queryset=ExState.objects.filter(TargetMonth=TargetMonth,depart_id=depart_id).order_by('task_id',))
        if not filterset.is_valid():
            raise ValidationError(filterset.errors)
        serializer = ExStateSerializer(instance=filterset.qs,many=True)
        return Response(serializer.data,status.HTTP_200_OK)

class ExStateRetriveAPIView(generics.RetrieveAPIView):
    """指定IDの詳細取得"""
    queryset = ExState.objects.all()
    serializer_class = ExStateSerializer
    lookup_field = 'id'

class ExStateUpDateAPIView(generics.UpdateAPIView):
    """指定IDの部分更新"""
    queryset = ExState.objects.all()
    serializer_class = ExStateSerializer
    lookup_field = 'id'

class ExStateCreateMonthAPIView(views.APIView):
    """月単位で実行状況データを作成する(実行した月)"""
    def post(self,request,*args,**kwargs):
        """MasTerDataからデータを取得する"""
        ExStateDatas =[] 
        Dept_filterset = DeptsFilter(request.query_params,queryset=DeptsMaster.objects.filter(valid_flg=True).order_by('id'))
        Task_filterset = TasksFilter(request.query_params,queryset=TasksMaster.objects.filter(valid_flg=True).order_by('id'))
        if( (Dept_filterset.is_valid() == False) or (Task_filterset.is_valid() == False)):
            raise ValidationError(filterset.errors)
        Dept_serializer = DeptsSerializer(instance=Dept_filterset.qs,many=True)
        Task_serializer = TasksSerializer(instance=Task_filterset.qs,many=True)
        DeptList = Dept_serializer.data
        TaskList = Task_serializer.data
        #対象月の取得方法を考えろ
        TargetMonth = "202106"
        for Dept in DeptList:
            for Task in TaskList:
                """OrderDictの要素では駄目とぬかすので"""
                Task_instance = TasksMaster(**Task)
                Dept_instance = DeptsMaster(**Dept)
                ExStateData = ExState(task=Task_instance,depart=Dept_instance,TargetMonth=TargetMonth)
                ExStateDatas.append(ExStateData)
        ExState.objects.bulk_create(ExStateDatas)
        #bulk_createは返り値を持たないためどのようにserializer.dataを表示させるか
        return Response(Dept_serializer.data,status.HTTP_200_OK)