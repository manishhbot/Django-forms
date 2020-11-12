from django.db import models
from django.contrib.auth.models import  User

# Create your models here.

class Details(models.Model):
    Name = models.CharField(max_length = 128)
    Phone = models.CharField(max_length = 128)
    Email = models.EmailField()

    def __str__(self):
        return self.Name
class Auth(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    Phone = models.CharField(max_length=20)

    def __str__(self):
        return self.user.username


