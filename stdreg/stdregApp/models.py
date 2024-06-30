from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100)
    studentid = models.CharField(max_length=100)
    email = models.EmailField()
    college = models.CharField(max_length=100)
    Dept = models.CharField(max_length=100)
    Year = models.CharField(max_length=100)
    gender = models.CharField(max_length=100)

    def __str__(self):
        return self.name
