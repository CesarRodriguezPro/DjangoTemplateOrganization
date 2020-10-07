from django.db import models
from django.contrib.auth.models import User, PermissionsMixin


class User(User, PermissionsMixin):
    def __str__(self):
        return "@{}".format(self.username)


class Company(models.Model):
    company_name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)

    def __str__(self):
        return self.company_name


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    is_owner = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    is_manager = models.BooleanField(default=False)
    is_systemAdmin = models.BooleanField(default=False)

    def __str__(self):
        return '{} {}'.format(User.first_name, User.last_name)


