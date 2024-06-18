from django import forms
from django.contrib.auth.models import User
from .models import CustomerProfile

class CustomerRegistrationForm(forms.ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class': 'form-control mb-3', 'placeholder': 'Write a password'}))
    confirm_password = forms.CharField(label='Confirm password', widget=forms.PasswordInput(attrs={'class': 'form-control mb-3', 'placeholder': 'Repeat your password'}))
    is_premium = forms.BooleanField(label='Are you premium?', required=False, widget=forms.CheckboxInput(attrs={'class': 'form-check-input m-auto mb-3 mt-2 ms-2'}))

    class Meta:
        model = User
        fields = ['username', 'password', 'confirm_password']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control mb-3', 'placeholder': 'Write a username'})
        }
        help_texts = {
            'username': None,
        }


class CustomerProfileForm(forms.ModelForm):
    class Meta:
        model = CustomerProfile
        fields = ['is_premium']