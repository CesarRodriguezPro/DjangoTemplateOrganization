from django.shortcuts import render, redirect
from .forms import OwnerCreateForm, EmployeesCreateForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required


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

    context = {
        'title': 'Sign up Owner',
        'form': form,
    }
    return render(request, "accounts/signup.html", context)


@login_required()
def registration_employees(request):
    if request.method == "POST":
        form = EmployeesCreateForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'Your Account has been Created! You are now able to log in')
            return redirect("accounts:login")
    else:
        form = EmployeesCreateForm()

    context = {
        'title': 'Sign up Employees',
        'form': form,
    }
    return render(request, "accounts/signup.html", context)


@login_required()
def profile_view(request):
    return render(request, "accounts/profile.html")

