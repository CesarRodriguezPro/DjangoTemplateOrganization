from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from .forms import OwnerCreateForm, EmployeesCreateForm, CompanyForm
from django.views.generic import CreateView, DetailView
from .models import User, Profile, Company
from django.contrib import messages
from django.contrib.auth.decorators import login_required

'''
still working in adding company id to profile and adding profile automatic
'''
def registration_owner(request):
    if request.method == "POST":
        form = OwnerCreateForm(request.POST)
        company = CompanyForm(request.POST)
        if form.is_valid() and company.is_valid():
            company.save()
            form.save()
            messages.success(request, f'Your Account has been Created! You are now able to log in')
            return redirect("accounts:login")
    else:
        form = OwnerCreateForm()
        company = CompanyForm()

    context = {
        'form': form,
        'company': company
    }
    return render(request, "accounts/signup_owner.html", context)


@login_required()
def registration_employees(request):
    if request.method == "POST":
        form = EmployeesCreateForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'Your Account has been Created! You are now able to log in')
            return redirect("accounts:login")
    else:
        form = OwnerCreateForm()

    context = {
        'form': form,

    }

    return render(request, "accounts/signup_employees.html", context)


@login_required()
def profile_view(request, username):
    user = User(username=username)
    profile = Profile(user=user)
    context = {
        'form': user.first_name,
        'profile': profile,
    }
    return render(request, "accounts/profile.html", context)

