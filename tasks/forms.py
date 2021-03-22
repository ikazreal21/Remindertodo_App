from django import forms
from django.forms import ModelForm
from .models import *


class TaskForms(forms.ModelForm):

    class Meta:
        model = Task
        fields = '__all__'

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control col-md-12 mb-3','placeholder':'Create Task'}),
            'completed': forms.CheckboxInput(attrs={'type': 'checkbox'}),

        }
