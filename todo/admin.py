from django.contrib import admin
from . models import DailyGoal, MonthlyGoal
# Register your models here.

@admin.register(DailyGoal)
class DailyAdmin(admin.ModelAdmin):
  list_display = ['name', 'date', 'day',  'task' ]

@admin.register(MonthlyGoal)
class MonthlyAdmin(admin.ModelAdmin):
  list_display = ['title','month', 'goals']