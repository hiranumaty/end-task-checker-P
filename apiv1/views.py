from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from depts.models import Depts
from .serializers import DeptsSerializer
# Create your views here.

class DeptsViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Depts.objects.all()
    serializer_class = DeptsSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]