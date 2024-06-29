from django.urls import path
from .views import RoutineListView, CreateRoutineView, TrainerRoutineListView, SelectRoutineView, DeleteRoutineView, RoutineDetailView, SearchTrainerRoutinesView

urlpatterns = [
    path('routines/', RoutineListView.as_view(), name='routine_list'),
    path('routines/<int:pk>/', RoutineDetailView.as_view(), name='routine_detail'),
    path('search_trainer_routines/', SearchTrainerRoutinesView.as_view(), name='search_trainer_routines'),   
    path('routines/create/', CreateRoutineView.as_view(), name='create_routine'),
    path('routines/trainer/<int:trainer_id>/', TrainerRoutineListView.as_view(), name='trainer_routine_list'),
    path('routines/select/<int:routine_id>/', SelectRoutineView.as_view(), name='select_routine'),
    path('routines/delete/<int:routine_id>/', DeleteRoutineView.as_view(), name='delete_routine'),
]