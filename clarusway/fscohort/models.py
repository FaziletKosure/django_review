from django.db import models

# Create your models here.
class Student(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    number = models.IntegerField()
    
    def __str__(self):
        return "{} {}".format(self.first_name, self.last_name) # Now it returns firt_name + last_name instead of Student object
    
     
