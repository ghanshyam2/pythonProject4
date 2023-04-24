from django import forms

from .models import *


class ToDoForm(forms.ModelForm):
    class Meta:
        model = ToDoModel
        fields = '__all__'
