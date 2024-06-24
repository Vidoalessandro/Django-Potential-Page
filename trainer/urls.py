from django.urls import path
from .views import TrainerRegistrationView, TrainerProfileView, TrainerProfileUpdateView, TrainerProfileDeleteView

urlpatterns = [
    path('signup/', TrainerRegistrationView.as_view(), name='signup-trainer'),
    path('profile-info/', TrainerProfileView.as_view(), name='profile-trainer'),
    path('profile-info/edit-profile', TrainerProfileUpdateView.as_view(), name='edit-profile-trainer'),
    path('profile-info/edit-profile/delete-profile/', TrainerProfileDeleteView.as_view(), name='delete_profile_trainer'),
]