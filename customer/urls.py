from django.urls import path
from .views import CustomerRegistrationView, CustomerProfileView, CustomerProfileUpdateView, CustomerProfileDeleteView

urlpatterns = [
    path('signup/', CustomerRegistrationView.as_view(), name='signup-customer'),
    path('profile-info/', CustomerProfileView.as_view(), name='profile-customer'),
    path('profile-info/edit-profile', CustomerProfileUpdateView.as_view(), name='edit-profile-customer'),
    path('profile-info/edit-profile/delete-profile/', CustomerProfileDeleteView.as_view(), name='delete_profile_customer'),
]