from django.urls import path
from .views import CustomerRegistrationView

urlpatterns = [
    path('signup/', CustomerRegistrationView.as_view(), name='signup-customer'),
]