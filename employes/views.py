from rest_framework import generics

from employes.models import Employes
from employes.serializers import EmployesSerializer


class EmployesView(generics.ListCreateAPIView):
    queryset = Employes.objects.all()
    serializer_class = EmployesSerializer


class EmployesDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Employes.objects.all()
    serializer_class = EmployesSerializer