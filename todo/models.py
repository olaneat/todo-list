from django.db import models
from django.utils import timezone
from . constant import days, months
# Create your models here.

class DailyGoal(models.Model):
  name = models.CharField(max_length = 150)
  day = models.CharField(max_length = 10, choices= days)
  date = models.DateField()
  task = models.TextField(max_length = 500)
  comments = models.TextField(max_length = 500, blank =True)
  

  def __str__(self):
  	return self.name


class MonthlyGoal(models.Model):
  title = models.CharField(max_length = 100)
  month = models.CharField(max_length = 10, choices = months)
  goals= models.TextField( max_length = 1000)
  comments = models.TextField(max_length = 500, blank = True)


  def __str__(self):
  	return self.title
   

