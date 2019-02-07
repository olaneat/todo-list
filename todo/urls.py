from . import views
from django.urls import path

urlpatterns = [
 path('', views.index, name = 'index'),
 path('daily_task', views.daily_activity, name = 'daily_activity'),
 path('monthly_goals', views.monthly_goals, name = 'monthly_goals'),
 path('add_task', views.add_task, name = 'add_task'),
 path('monthly_goals_list', views.MonthlyGoalListView.as_view(), name = 'monthly_goals_list'),
 path('monthly_goal/<int:pk>/', views.MonthlyGoalDetailView.as_view(), name = 'month_goal_detail'),
 path('display_task', views.display_goals, name = 'display_task' ),
 path('daily_goal', views.DailyGoalListView.as_view(), name = 'daily_goal_list'),
 path('daily_goal/<int:pk>', views.DailyGoalDetailView.as_view(), name = 'daily_goal_detail'),



]
