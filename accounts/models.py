from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics',null=True, blank=True)


class Owner(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE,null=True)


class Company(models.Model):
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE,null=True)
    company_name = models.CharField(max_length=100, unique=True, null=True)
    address = models.CharField(max_length=100,null=True)

    def __str__(self):
        return self.company_name


class Employee(models.Model):

    STATUS_CHOICES = [
        ("Admin", "Admin"),
        ("Manager", "Manager"),
        ("sysAdmin", "System Admin")
    ]

    profile = models.ForeignKey(Profile, on_delete=models.CASCADE,null=True)
    role = models.CharField(choices=STATUS_CHOICES, max_length=10,null=True)
    company = models.ForeignKey(Company, on_delete=models.CASCADE,null=True)


