from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView
from django.contrib.auth.models import User
from .form import TrainerRegistrationForm
from . models import TrainerProfile
from django.urls import reverse_lazy
from django.contrib.auth import login

# Create your views here.
class TrainerRegistrationView(CreateView):
    template_name = 'trainer/signup.html'
    form_class = TrainerRegistrationForm
    success_url = reverse_lazy('home')
    
    
    def form_valid(self, form):

        password = form.cleaned_data['password']
        confirm_password = form.cleaned_data['confirm_password']
        if password != confirm_password:

            return self.render_to_response(self.get_context_data(form=form, password_error='Passwords do not match'))

        username = form.cleaned_data['username']
        specialty = form.cleaned_data['specialty']
        
        if User.objects.filter(username=username).exists():
            return self.render_to_response(self.get_context_data(form=form, username_error='This username is already taken.'))
        
        user = User.objects.create_user(username=username, password=password)

        trainer = TrainerProfile.objects.create(user=user, specialty=specialty)
        
        login(self.request, user)

        return redirect(self.success_url)
    
    def form_invalid(self, form):
        context = self.get_context_data(form=form)
        context['password_error'] = form.errors.get('confirm_password')
        return self.render_to_response(context)