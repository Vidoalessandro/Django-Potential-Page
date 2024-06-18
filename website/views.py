from django.shortcuts import render, redirect
from django.views.generic import TemplateView, View
from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.views import View
from django.contrib import messages
from django.http import HttpResponse
from django.template.loader import get_template

# Create your views here.

class HomeView(TemplateView):
    template_name = 'website/home.html'

class SigninView(TemplateView):
    template_name = 'website/signin.html'
    
class CustomLoginView(View):
    template_name = 'website/login.html'

    def get(self, request):
        form = AuthenticationForm()
        return render(request, self.template_name,  {'form': form})

    def post(self, request):
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
        else:
            error_msg = 'Invalid username or password.'
            messages.error(request, error_msg)
            return render(request, self.template_name, {'form': form})
    
class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('home')