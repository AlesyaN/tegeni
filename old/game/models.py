from django.db import models

# Create your models here.

class Levels(models.Model):
    name  = models.TextField()
    img = models.ImageField(upload_to='game',
                      height_field=100, width_field=100)
    val = models.CharField(max_length = 6);

def __str__(self):
    return self.title
