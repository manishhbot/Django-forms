from django.db import models

# Create your models here.

class Details(models.Model):
    Name = models.CharField(max_length = 128)
    Phone = models.CharField(max_length = 128)
    Email = models.EmailField()

    def __str__(self):
        return self.Name


