from django.db import models

# Create your models here.
class Review(models.Model):
    objects = models.Manager() # this is needed to avoid VS Code error
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.CharField(max_length=20)
    review = models.CharField(max_length=200)
    