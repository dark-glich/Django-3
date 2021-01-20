from django import forms
from .models import task

class create_task_form(forms.ModelForm):
    class Meta:
        model = task
        fields = ['task_text', 'user']
        widgets = {
                'task_text': forms.TextInput(attrs={'class': 'form-task', 'placeholder': 'Write Your Notes', 'id':"myInput"})}

