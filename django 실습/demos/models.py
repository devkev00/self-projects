from django.db import models

# Create your models here.
class Cal(models.Model):
  first_num= models.IntegerField()
  second_num=models.IntegerField()
  operator=models.TextField()
  result=models.IntegerField()