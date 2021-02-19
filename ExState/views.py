from django_filters import rest_framework as filters
from rest_framework import status, generics,views
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response

from .models import ExState
from .serializers import ExStateSerializer
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


class ExStateListAPIView(generics.ListAPIView):
    """一覧の総取得"""
    queryset = ExState.objects.all()
    serializer_class = ExStateSerializer
    filter_backends = [filters.DjangoFilterBackend]
    filterset_fields = '__all__'

#uuidで取得することにした
class ExStateRetriveAPIView(generics.RetrieveAPIView):
    queryset = ExState.objects.all()
    serializer_class = ExStateSerializer

#見るだけのクラスも作ってみた
# class ExStateRetriveAPIView(
#         MultipleFieldLookupMixin,
#         generics.RetrieveAPIView):
#     print("a")
#     serializer_class = ExStateSerializer
#     queryset = ExState.objects.all()
#     lookup_fields = ('deploy_id', 'Task_id')




# class ExStateRetriveUpdateAPIView(
#         MultipleFieldLookupMixin,
#         generics.RetrieveUpdateAPIView):
#     """詳細の取得"""
    
#     serializer_class = ExStateSerializer
#     queryset = ExState.objects.all()
#     lookup_fields = ('deploy_id', 'Task_id')
