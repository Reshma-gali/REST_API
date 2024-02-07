from django.db import models

# Create your models here.
class Books(models.Model):
    Book_Name = models.CharField(max_length=50)
    Author_Name= models.CharField(max_length=50)
    price = models.IntegerField()