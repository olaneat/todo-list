from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import DailyGoal, MonthlyGoal
from .forms import DailyGoalForm, MonthlyGoalForm
from django.views import generic


def index(request):
  return render(request, 'todo/index.html')

def add_task(request):
  return render(request, 'todo/select_task.html')


def daily_activity(request):
  daily_activity = DailyGoalForm(request.POST or None)
  if request.method == 'POST' and daily_activity.is_valid():
    daily_activity.save()
    return HttpResponse("Congrats!!! You've sucessfully added the task for the day")
  else:
  	daily_activity = DailyGoalForm()

  return render(request, 'todo/dailytask.html',\
   {'daily_activity': daily_activity})


def monthly_goals(request):
  monthly_goal = MonthlyGoalForm(request.POST or None)
  if request.method == 'POST' and monthly_goal.is_valid():
    monthly_goal.save()
    return HttpResponse("success, your Goals for the month has been added")
  else:
  	monthly_goal = MonthlyGoalForm()

  return render(request, 'todo/monthly_activities.html',\
   {'monthly_goal': monthly_goal})

class MonthlyGoalListView(generic.ListView):
  model = MonthlyGoal
  template_name = 'todo/month_goal.html'

class MonthlyGoalDetailView(generic.DetailView):
  model = MonthlyGoal
  template_name = 'todo/monthly_goal.html'

class DailyGoalListView(generic.ListView):
  model = DailyGoal
  template_name = 'todo/dailygoal_list.html'
  #queryset = DailyGoal.objects.all()[:10]
  paginate_by = 15


class DailyGoalDetailView(generic.DetailView):
  model = DailyGoal
  template_name = 'todo/dailygoal_detail.html'

def display_goals(request):
    return render(request, 'todo/goals.html')
