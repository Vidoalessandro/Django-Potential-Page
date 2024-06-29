from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Exercise

# Create your views here.
class ExerciseListView(ListView):
    model = Exercise
    template_name = 'exercises/exercises.html'
    context_object_name = 'exercises'
    paginate_by = 10  # Opcional, para paginar la lista si hay muchos ejercicios

    def get_queryset(self):
        queryset = super().get_queryset()
        query = self.request.GET.get('q')
        if query:
            queryset = queryset.filter(name__icontains=query)
        return queryset

class ExerciseDetailView(DetailView):
    model = Exercise
    template_name = 'exercises/exercise_info.html'
    context_object_name = 'exercise'