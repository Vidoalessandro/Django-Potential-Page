from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.
class TrainerProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    specialty = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    is_verified = models.BooleanField(default=False)
    creation_date = models.DateTimeField(default=timezone.now)
    profile_picture = models.ImageField(upload_to='users/', default='users/user_image.png')
    profile_picture_url = models.URLField(blank=True)
    
    def __str__(self):
        return self.user.username