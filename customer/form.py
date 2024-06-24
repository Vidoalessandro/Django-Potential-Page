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
        
class EditCustomerProfileForm(forms.ModelForm):
    username = forms.CharField(max_length=150,widget=forms.TextInput(attrs={'class': 'form-control mb-3', 'placeholder': 'Write a username'}))
    
    class Meta:
        model = CustomerProfile
        fields = ['profile_picture', 'description']
        widgets = {
            'profile_picture': forms.FileInput(attrs={'class': 'form-control mb-3'}),
            'description': forms.Textarea(attrs={'class': 'form-control mb-3', 'placeholder': 'Write a description', 'rows': 5}),
        }

        
    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user')
        super().__init__(*args, **kwargs)
        self.fields['username'].initial = user.username
        
    def clean_username(self):
        username = self.cleaned_data['username']
        if User.objects.filter(username=username).exists() and username != self.instance.user.username:
            raise forms.ValidationError('This username is already taken. Please try another one.')
        return username