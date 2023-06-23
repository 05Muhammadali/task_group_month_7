from django import forms

from .models import Employes


class EmployesForm(forms.ModelForm):
    class Meta:
        model = Employes
        fields = ['name', 'employment_position', 'employment_start_date', 'salary', 'parent']