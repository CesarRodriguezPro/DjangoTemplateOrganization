from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from .models import Company
from django import forms


class CompanyForm(forms.ModelForm):

    class Meta:
        model = Company
        fields = ('company_name', 'address')


class OwnerCreateForm(UserCreationForm):

    class Meta:
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')
        model = get_user_model()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].label = 'Display Name'
        self.fields['email'].label = "Email Address"


class EmployeesCreateForm(UserCreationForm):
    is_admin = forms.BooleanField(required=False)
    is_manager = forms.BooleanField(required=False)
    is_systemAdmin = forms.BooleanField(required=False)

    class Meta:
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')
        model = get_user_model()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].label = 'Display Name'
        self.fields['email'].label = "Email Address"