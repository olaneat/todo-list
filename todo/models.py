from django.db import models
from django.utils import timezone
from . constant import days, months
from django.shortcuts import reverse
# Create your models here.

class DailyGoal(models.Model):
  title = models.CharField(max_length = 200)
  day = models.CharField(max_length = 10, choices= days)
  date = models.DateField()
  task = models.TextField(max_length = 500)
  comments = models.TextField(max_length = 500, blank =True)

  class Meta:
    ordering = ['-date']


  def __str__(self):
  	return self.title

  def get_absolute_url(self):
      return reverse('daily_goal_detail', args =[str(self.id)])

class MonthlyGoal(models.Model):
  title = models.CharField(max_length = 100)
  month = models.CharField(max_length = 10, choices = months)
  goals= models.TextField( max_length = 1000)
  comments = models.TextField(max_length = 500, blank = True)


  def __str__(self):
  	return self.title

  def get_absolute_url(self):
    return  reverse ('month_goal_detail', args = [str(self.id)])
