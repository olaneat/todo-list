from django.forms import ModelForm, CharField, Textarea
from . models import DailyGoal, MonthlyGoal


class DailyGoalForm(ModelForm):
  
  class Meta:
  	model = DailyGoal
  	fields = '__all__'
  
class MonthlyGoalForm(ModelForm):

  class Meta:
    model = MonthlyGoal
    fields ='__all__' 