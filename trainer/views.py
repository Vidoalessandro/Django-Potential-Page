from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView
from django.views import View
from django.contrib.auth.models import User
from .form import TrainerRegistrationForm, EditTrainerProfileForm
from . models import TrainerProfile
from django.urls import reverse_lazy
from django.contrib.auth import login, logout
from django.contrib.auth.mixins import LoginRequiredMixin

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
    
class TrainerProfileView(View):
    template_name = 'trainer/profile_info.html'

    def get(self, request):
        if request.user.is_authenticated and hasattr(request.user, 'trainerprofile'):
            profile = request.user.trainerprofile
            context = {
                'profile': profile,
                'type': 'trainer'
            }
            return render(request, self.template_name, context)
        else:
            return redirect('home')

class TrainerProfileUpdateView(UpdateView):
    model = TrainerProfile
    form_class = EditTrainerProfileForm
    template_name = 'trainer/edit_profile.html'
    success_url = reverse_lazy('profile-trainer')
    
    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    def form_valid(self, form):
        user = self.request.user
        user.username = form.cleaned_data['username']
        user.save()
        return super().form_valid(form)

    def get_object(self, queryset=None):
        return self.request.user.trainerprofile
    
class TrainerProfileDeleteView(LoginRequiredMixin, View):
    success_url = reverse_lazy('home')

    def post(self, request, *args, **kwargs):
        user = request.user
        user.delete()
        logout(request)
        return redirect(self.success_url)