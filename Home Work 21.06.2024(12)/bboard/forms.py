from django.forms import ModelForm
from .models import Bb
from django import forms
from .models import Task

class BbForm(ModelForm):
    class Meta:
        model = Bb
        fields = ('title', 'content', 'price', 'rubric', 'published')
        
class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['description'] 
        labels = {
            'description': 'Описание'  
        }