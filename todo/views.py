from django.shortcuts import render, redirect, get_object_or_404
from .models import DailyGoal, MonthlyGoal
from .forms import DailyGoalForm, MonthlyGoalForm

def index(request):
  return render(request, 'index.html')

def add_task(request):
  return render(request, 'select_task.html')


def daily_activity(request):
  daily_activity = DailyGoalForm(request.POST or None)
  if request.method == 'POST' and daily_activity.is_valid():
    daily_activity.save()
  else:
  	daily_activity = DailyGoalForm()
  
  return render(request, 'dailytask.html',\
   {'daily_activity': daily_activity})


def monthly_goals(request):
  monthly_goal = MonthlyGoalForm(request.POST or None)
  if request.method == 'POST' and monthly_goal.is_valid():
  	monthly_goal.save()
  else:
  	monthly_goal = MonthlyGoalForm()
  
  return render(request, 'monthly_activities.html',\
   {'monthly_goal': monthly_goal})

def task_added(request):
  return render(request, 'notification_page.html')


def display_goals(request):
  task = get_object_or_404(DailyGoal)
  return render(request, 'goals.html', {'task': task})

def daily_goal(request):
  return render(request, 'day_goal.html')

def monthly_accomplishment(request):
  return render (request, 'month_goal.html')