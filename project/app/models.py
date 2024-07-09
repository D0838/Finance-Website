from django.db import models
from datetime import date

class Contact(models.Model):
    name= models.CharField(max_length=122)
    email = models.CharField(max_length=122)
    phone = models.CharField(max_length=10)
    add= models.CharField(max_length=122) 
    date = models.DateField(default=date.today)
    def __str__(self):
        return self.name
    