from django.db import models

# Create your models here.

# BSS information
class teacher (models.Model):
    Name = models.CharField(max_length=25)
    Area = models.CharField(max_length=30)
    Course = models.CharField(max_length=20)
    
# manual information