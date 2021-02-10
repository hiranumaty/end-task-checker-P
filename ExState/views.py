from django_filters import rest_framework as filters
from rest_framework import status,generics
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response

from .models import ExState
from .serializers import ExStateSerializer

class ExStateListAPIView(generics.ListAPIView):
    queryset = ExState.objects.all()
    serializer_class = ExStateSerializer
    filter_backends =[filters.DjangoFilterBackend]
    filterset_fields = '__all__'