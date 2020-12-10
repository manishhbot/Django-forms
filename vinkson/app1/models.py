from django.db import models


# Create your models here.

class ContactDetails(models.Model):
    Name = models.CharField(max_length=120)
    Email = models.EmailField()
    Phone = models.CharField(max_length=120)
    Company = models.CharField(max_length=120)

    def __str__(self):
        return self.Name
