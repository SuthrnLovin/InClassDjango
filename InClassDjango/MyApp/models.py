from django.db import models



class teacher (models.Model):
    Name = models.CharField(max_length=25)
    Area = models.CharField(max_length=30)

x = 'This is the outline'



# BSS information
class teacher (models.Model):
    Name = models.CharField(max_length=25)
    Area = models.CharField(max_length=30)

class Unit (models.Model):
    Title = models.CharField(max_length=25)
    Outline = x
    
    
# manual information 

