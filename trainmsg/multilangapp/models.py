from django.db import models

# Create your models here.

class Multilangapp(models.Model):
    train_No = models.BigIntegerField()
    train_name=models.CharField(max_length=100)
    train_source=models.CharField(max_length=100)
    train_destn=models.CharField(max_length=100)
    arrivaldatatime=models.DateTimeField()#models.DateTimeField()
    platformNo=models.IntegerField()

    def __str__(self):
        return self.train_name


