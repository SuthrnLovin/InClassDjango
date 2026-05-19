from django.db import models
from django.core.validators import FileExtensionValidator

class AudioFile(models.Model):
    title = models.CharField(max_length=100)
    audio = models.FileField(upload_to='audio/',validators=[FileExtensionValidator(['mp3'])])


class teacher (models.Model):
    Name = models.CharField(max_length=25)
    Area = models.CharField(max_length=30)
    

class Unit (models.Model):
    Title = models.CharField(max_length=25)
    Outline = models.CharField(max_length=25)
    
    
# manual information 

