from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from .forms import OwnerCreateForm, EmployeesCreateForm
from django.views.generic import CreateView, DetailView
from .models import User, Profile, Company


class RegistrationOwner(CreateView):
    form_class = OwnerCreateForm
    success_url = reverse_lazy('accounts:login')
    template_name = 'accounts/signup_owner.html'


def registration_employees(response):
    if response.method == "POST":
        form = EmployeesCreateForm(response.POST)
        if form.is_valid():
            user = form.save()
            # user.profile.company.company_name = owner_user_company
            # user.profile.company.address = owner_user_company_address
            return redirect("accounts:login")
    return render(response, "accounts/signup_employees.html", {'form': EmployeesCreateForm})


///// keep working in make the profile page

def profile_view(request, username):
    user = User(username=username)
    profile = Profile(user=user.pk)

    context = {
        'form': user.first_name,
        'profile': profile,
    }


    return render(request, "accounts/profile.html", context)

