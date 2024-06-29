from django.urls import path
from .views import ExerciseListView, ExerciseDetailView

urlpatterns = [
    path('excercises-list/', ExerciseListView.as_view(), name='exercises-list'),
    path('exercise/<int:pk>/', ExerciseDetailView.as_view(), name='exercise-detail'),
]