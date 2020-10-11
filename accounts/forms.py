from django.contrib.auth.forms import UserCreationForm
from .models import Owner, Employee, Company
from django import forms


class OwnerCreateForm(forms.ModelForm):

    class Meta:
        fields = '__all__'
        model = Owner


class EmployeesCreateForm(forms.ModelForm):

    class Meta:
        fields = '__all__'
        model = Employee
