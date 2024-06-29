from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from django.views.generic import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .models import Routine
from trainer.models import TrainerProfile
from .form import RoutineForm
# Create your views here.

class RoutineListView(LoginRequiredMixin, View):
    template_name = 'routines/routine_list.html'

    def get(self, request, *args, **kwargs):
        user = request.user
        if hasattr(user, 'customerprofile'):
            routines = user.customerprofile.routines.all()
        else:
            routines = Routine.objects.filter(trainer=user.trainerprofile)

        context = {
            'routines': routines,
        }
        return render(request, self.template_name, context)


class TrainerRoutineListView(LoginRequiredMixin, View):
    template_name = 'routines/trainer_routine_list.html'

    def get(self, request, trainer_id, *args, **kwargs):
        trainer = get_object_or_404(TrainerProfile, id=trainer_id)
        routines = Routine.objects.filter(trainer=trainer)
        context = {
            'routines': routines,
            'trainer': trainer,
        }
        return render(request, self.template_name, context)

class SelectRoutineView(LoginRequiredMixin, View):
    def post(self, request, routine_id, *args, **kwargs):
        routine = get_object_or_404(Routine, id=routine_id)
        request.user.customerprofile.routines.add(routine)
        return redirect('routine_list')

class CreateRoutineView(LoginRequiredMixin, View):
    template_name = 'routines/create_routine.html'
    form_class = RoutineForm

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            routine = form.save(commit=False)
            routine.trainer = request.user.trainerprofile
            routine.save()
            return redirect('routine_list')
        return render(request, self.template_name, {'form': form})


class DeleteRoutineView(LoginRequiredMixin, View):
    def post(self, request, routine_id, *args, **kwargs):
        routine = get_object_or_404(Routine, id=routine_id)
        if request.user.trainerprofile == routine.trainer:
            routine.delete()
        elif request.user.customerprofile:
            request.user.customerprofile.routines.remove(routine)
        return redirect('routine_list')
    
class RoutineDetailView(DetailView):
    model = Routine
    template_name = 'routines/routine_detail.html'  # Asegúrate de tener este template creado
    context_object_name = 'routine'
    
class SearchTrainerRoutinesView(LoginRequiredMixin, View):
    template_name = 'routines/search_trainer_routines.html'

    def get(self, request):
        trainer_name = request.GET.get('trainer_name')

        if trainer_name:
            try:
                trainer = TrainerProfile.objects.get(user__username=trainer_name)
                routines = Routine.objects.filter(trainer=trainer)
            except TrainerProfile.DoesNotExist:
                trainer = None
                routines = []
        else:
            trainer = None
            routines = []

        context = {
            'trainer_name': trainer_name,
            'trainer': trainer,
            'routines': routines,
        }
        return render(request, self.template_name, context)