from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100,null=False)
    rollno = models.IntegerField(null=False)
    std = models.IntegerField()

    def __str__(self): 
        return self.name

# Create your models here.
