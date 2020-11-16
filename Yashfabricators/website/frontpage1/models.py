from django.db import models
from django.contrib.auth.models import User


# Create your models here.
# class AddUser(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     social_media = models.URLField()
#
#     def __str__(self):
#         return self.user.username


class ContactDetails(models.Model):
    Name = models.CharField(max_length=20)
    Email = models.EmailField()
    Phone_number = models.CharField(max_length=20)
    Company = models.CharField(max_length=30)

    def __str__(self):
        return self.Name
