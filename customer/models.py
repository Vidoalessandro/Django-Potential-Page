from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from routines.models import Routine

# Create your models here.
class CustomerProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    creation_date = models.DateTimeField(default=timezone.now)
    is_premium = models.BooleanField(default=False)
    profile_picture = models.ImageField(upload_to='users/', default='users/user_image.png')
    profile_picture_url = models.URLField(blank=True)
    routines = models.ManyToManyField(Routine, related_name='customers', blank=True)
    
    def __str__(self):
        return self.user.username