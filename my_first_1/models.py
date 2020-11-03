from django.db import models

class Freedemo(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    email = models.EmailField(unique=True)
    address = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Registrations(models.Model):
    name = models.ForeignKey(Freedemo, on_delete=models.CASCADE)
    job = models.CharField(max_length=100)

    def __str__(self):
        return self.course

class Onboarded(models.Model):
    name = models.ForeignKey(Registrations, on_delete=models.CASCADE)
    time = models.TimeField()

    def __str__(self):
        return self.name

