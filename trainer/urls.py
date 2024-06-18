from django.urls import path
from .views import TrainerRegistrationView

urlpatterns = [
    path('signup/', TrainerRegistrationView.as_view(), name='signup-trainer'),
]