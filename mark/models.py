from os import name
from django.db import models

# Create your models here.
class Student(models.Model):
    idno=models.IntegerField(max_length=1000,primary_key=True)
    name=models.CharField(max_length=1000)
    m1=models.IntegerField(max_length=1000)
    m2=models.IntegerField(max_length=1000)
    m3=models.IntegerField(max_length=1000)
    average=models.FloatField()
    grade=models.CharField(max_length=10)