from django import forms
from django.contrib.auth.models import User
from .models import TrainerProfile

class TrainerRegistrationForm(forms.ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class': 'form-control mb-3', 'placeholder': 'Write a password'}))
    confirm_password = forms.CharField(label='Confirm password', widget=forms.PasswordInput(attrs={'class': 'form-control mb-3', 'placeholder': 'Repeat your password'}))
    specialty = forms.CharField(max_length=100, label='Specialty', widget=forms.TextInput(attrs={'class': 'form-control mb-3', 'placeholder': 'Write a specialty'}))

    class Meta:
        model = User
        fields = ['username', 'password', 'confirm_password']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control mb-3', 'placeholder': 'Write a username'})
        }
        help_texts = {
            'username': None,
        }

class TrainerProfileForm(forms.ModelForm):
    class Meta:
        model = TrainerProfile
        fields = ['specialty']