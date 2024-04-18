from django.db import models

from django.db import models

class Recipe(models.Model):
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=64, unique=True)
    text = models.CharField(max_length=300)
    
