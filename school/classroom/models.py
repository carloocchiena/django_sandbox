from django.db import models

# Create your models here.
class Teacher(models.Model):
    objects = models.Manager() # this is needed to avoid VS Code error
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    subject = models.CharField(max_length=20)
    
    def __str__(self):
        return f"{self.first_name}, {self.last_name}, {self.subject}"
     