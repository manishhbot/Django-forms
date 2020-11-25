from django.db import models

class School(models.Model):
    Name = models.CharField(max_length=120)
    Board = models.CharField(max_length=120)
    Location = models.CharField(max_length=120)

    def __str__(self):
        return self.Name

class Student(models.Model):
    Name = models.CharField(max_length=120)
    Class = models.PositiveIntegerField()
    school = models.ForeignKey(School, related_name='students', on_delete=models.CASCADE)

    def __str__(self):
        return self.Name
