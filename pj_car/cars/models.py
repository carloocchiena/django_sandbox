from django.db import models

# Create your models here.
class Car(models.Model):
    objects = models.Manager() # this is needed to avoid VS Code error
    brand = models.CharField(max_length=30)
    year = models.IntegerField()
    
    def __str__(self):
        return f'This is a {self.brand} from {self.year}'
      