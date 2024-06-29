from django.db import models
from trainer.models import TrainerProfile

# Create your models here.
class Routine(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    trainer = models.ForeignKey(TrainerProfile, on_delete=models.SET_NULL, null=True, blank=True, default=None)
    
    def __str__(self):
        return self.name