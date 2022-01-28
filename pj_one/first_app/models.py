from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.
class MyModel(models.Model):
    objects = models.Manager() # this is needed to avoid VS Code error
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    age = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(120)])
    rate = models.IntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(5)])
        
    def __str__(self):
        return self.first_name + ' ' + self.last_name
    