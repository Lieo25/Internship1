from django.db import models


# Create your models here.
class Student(models.Model):
    name=models.CharField(max_length=100)
    rollno=models.IntegerField()
    date=models.DateField()
    one=models.CharField(max_length=100,blank=True)
    two=models.CharField(max_length=100,blank=True)
    three=models.CharField(max_length=100,blank=True)
    four=models.CharField(max_length=100,blank=True)
    five=models.CharField(max_length=100,blank=True)
    six=models.CharField(max_length=100,blank=True)
    seven=models.CharField(max_length=100,blank=True)

    def __str__(self):
        return self.name
