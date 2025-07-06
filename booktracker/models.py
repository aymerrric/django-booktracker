from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
# Create your models here.

class Book(models.Model):
    name = models.CharField(max_length=200)
    read = models.BooleanField("Already read ?", name="status")
    pages = models.IntegerField()
    note = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(20)])
