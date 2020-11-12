from django.db import models
from django.contrib.auth.models import User

# Create your models here.

GENDER_CHOICE = (
    (u'M', u'Male'),
    (u'F', u'Female'),
)


class Details(models.Model):
    phone = models.CharField(max_length=123)
    age = models.CharField(max_length=2)
    gender = models.CharField(max_length=2, choices=GENDER_CHOICE)

    def __str__(self):
        return self.phone


class Django_user(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    picture = models.ImageField(upload_to='images', blank=True)

    def __str__(self):
        return self.user.username
