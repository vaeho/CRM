from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    company = models.CharField(max_length=100)

    def __str__(self):
        return self.username

class Record(models.Model):
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=150)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=100)
    last_contacted = models.DateField(default=None, null=True, blank=True)

    def __str__(self):
        return self.name