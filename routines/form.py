from django import forms
from .models import Routine

class RoutineForm(forms.ModelForm):
    class Meta:
        model = Routine
        fields = ['name', 'description']
        labels = {
            'name': 'Routine Name',
            'description': 'Description',
        }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control mb-3', 'placeholder': 'Enter routine name'}),
            'description': forms.Textarea(attrs={'class': 'form-control mb-3', 'placeholder': 'Enter description', 'rows': 5}),
        }