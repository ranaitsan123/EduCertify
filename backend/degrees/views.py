# backend/degrees/views.py

from rest_framework import viewsets
from .models import Degree
from .serializers import DegreeSerializer

class DegreeViewSet(viewsets.ModelViewSet):
    queryset = Degree.objects.all()
    serializer_class = DegreeSerializer
