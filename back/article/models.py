from turtle import update
from django.db import models

# Create your models here.
class Article(models.Model):

    title = models.CharField(max_length=255)
    creation_date = models.DateField(auto_now_add=True)
    update_date = models.DateField(auto_now=True)
    content = models.TextField() 


    