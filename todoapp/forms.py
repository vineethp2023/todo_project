from .models import Task
from django import forms

# creates form from model named Task
class TodoForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['name', 'date', 'priority']
