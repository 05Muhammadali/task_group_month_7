from rest_framework import serializers
from employes.models import Employes


class EmployesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employes
        fields = ("id", "name", "employment_position", "employment_start_date", "salary", "date_added", "parent")