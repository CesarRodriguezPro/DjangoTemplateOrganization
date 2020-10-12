from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):

    STATUS_CHOICES = [
        ("Admin", "Admin"),
        ("Manager", "Manager"),
        ("sysAdmin", "System Admin"),
        ("Employee", "Employee")
    ]

    image = models.ImageField(default='default.jpg', upload_to='profile_pics', null=True, blank=True)
    role = models.CharField(choices=STATUS_CHOICES, max_length=10, null=True)
    is_owner = models.BooleanField(default=False, blank=True, null=True)

    def __str__(self):
        return f"@{self.username}"


class Companies(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    company_name = models.CharField(max_length=100, unique=True, null=True)
    address = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.company_name




