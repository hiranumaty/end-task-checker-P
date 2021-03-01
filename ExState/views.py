from django_filters import rest_framework as filters
from rest_framework import status, generics,views
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response
from .models import ExState
from MasterData.models import TasksMaster,DeptsMaster
from .serializers import ExStateSerializer
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
class GetDeptsMaster(generics.ListAPIView):
    queryset = DeptsMaster.objects.all()
    serializer_class = DeptsSerializer
    filter_backends = [filters.DjangoFilterBackend]
    filterset_fields = '__all__'
class GetTasksMaster(generics.ListAPIView):
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
#Filterを用いて検索を行う
class ExStateListMonthAPIView(views.APIView):
    def get(self,request,TargetMonth,*args,**kwargs):
        #フィルターをどうかけるか
        filterset = ExStateFilter(request.query_params,queryset=ExState.objects.filter(TargetMonth=TargetMonth).order_by('depart_id','task_id'))
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


