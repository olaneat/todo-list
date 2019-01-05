from . import views
from django.urls import path

urlpatterns = [
 path('', views.index, name = 'index'),
 path('daily_task', views.daily_activity, name = 'daily_activity'),
 path('notification', views.task_added, name = 'task_added' ),
 path('monthly_goals', views.monthly_goals, name = 'monthly_goals'),
 path('add_task', views.add_task, name = 'add_task'),
 path('display', views.display_goals, name = 'display_goals'),
 path('daily_goal', views.daily_goal, name = 'daily_goal'),
 path('monthly_accomplishment', views.monthly_accomplishment, name = 'monthly_accomplishment'),




]