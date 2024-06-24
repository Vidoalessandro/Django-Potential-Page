from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView
from django.views import View
from django.contrib.auth.models import User
from .form import CustomerRegistrationForm, CustomerProfileForm, EditCustomerProfileForm
from . models import CustomerProfile
from django.urls import reverse_lazy
from django.contrib.auth import login, logout
from django.contrib.auth.mixins import LoginRequiredMixin

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
    
class CustomerProfileView(View):
    template_name = 'customer/profile_info.html'

    def get(self, request):
        if request.user.is_authenticated and hasattr(request.user, 'customerprofile'):
            profile = request.user.customerprofile
            context = {
                'profile': profile,
                'type': 'customer'
            }
            return render(request, self.template_name, context)
        else:
            return redirect('home')
        
class CustomerProfileUpdateView(UpdateView):
    model = CustomerProfile
    form_class = EditCustomerProfileForm
    template_name = 'customer/edit_profile.html'
    success_url = reverse_lazy('profile-customer')
    
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
        return self.request.user.customerprofile
    
class CustomerProfileDeleteView(LoginRequiredMixin, View):
    success_url = reverse_lazy('home')

    def post(self, request, *args, **kwargs):
        user = request.user
        user.delete()
        logout(request)
        return redirect(self.success_url)