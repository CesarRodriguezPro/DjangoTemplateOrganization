from django.db import models
from django.contrib.auth.models import User, PermissionsMixin


class User(User, PermissionsMixin):
    def __str__(self):
        return "@{}".format(self.username)


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    middle_name = models.CharField(max_length=30, blank=True)
    dob = models.DateField(null=True, blank=True)