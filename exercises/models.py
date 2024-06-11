from django.db import models

# Create your models here.
class Exercise(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    muscle_group = models.CharField(max_length=100)
    image = models.ImageField(upload_to='exercises/', default='exercises/exercise_image.png')
    youtube_link = models.URLField(blank=True)
    
    def __str__(self):
        return self.name