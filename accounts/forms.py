from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django import forms


class OwnerCreateForm(UserCreationForm):

    company = forms.CharField(max_length=100)
    company_address = forms.CharField(max_length=100)
    is_owner = forms.BooleanField(required=True)

    class Meta:
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')
        model = get_user_model()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].label = 'Display Name'
        self.fields['email'].label = "Email Address"


class EmployeesCreateForm(UserCreationForm):

    is_admin = forms.BooleanField()
    is_manager = forms.BooleanField()
    is_systemAdmin = forms.BooleanField()

    class Meta:
        fields = ('username', 'email', 'password1', 'password2')
        model = get_user_model()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].label = 'Display Name'
        self.fields['email'].label = "Email Address"