from django import forms
from .models import Task

class TaskForm(forms.ModelForm):
    deadline = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'}),
        input_formats=['%Y-%m-%d']
    )

    class Meta:
        model = Task
        fields = ['title', 'description', 'deadline', 'completed']
