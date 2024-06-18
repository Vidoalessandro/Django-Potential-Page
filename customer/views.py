from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView
from django.contrib.auth.models import User
from .form import CustomerRegistrationForm
from . models import CustomerProfile
from django.urls import reverse_lazy
from django.contrib.auth import login

# Create your views here.
class CustomerRegistrationView(CreateView):
    template_name = 'customer/signup.html'
    form_class = CustomerRegistrationForm
    success_url = reverse_lazy('home')
    
    
    def form_valid(self, form):

        password = form.cleaned_data['password']
        confirm_password = form.cleaned_data['confirm_password']
        is_premium = form.cleaned_data['is_premium']
        if password != confirm_password:

            return self.render_to_response(self.get_context_data(form=form, password_error='Passwords do not match'))

        username = form.cleaned_data['username']
        user = User.objects.create_user(username=username, password=password)

        customer = CustomerProfile.objects.create(user=user, is_premium=is_premium)
        
        login(self.request, user)

        return redirect(self.success_url)
    
    def form_invalid(self, form):
        context = self.get_context_data(form=form)
        context['password_error'] = form.errors.get('confirm_password')
        return self.render_to_response(context)