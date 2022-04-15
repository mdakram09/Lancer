from django.db import models

# Create your models here.
class Workforusform(models.Model):
     sno= models.AutoField(primary_key=True)
     name= models.CharField(max_length=255)
     phone= models.CharField(max_length=13)
     email= models.CharField(max_length=100)
     paddress= models.CharField(max_length=255)
     pan= models.CharField(max_length=255)
     date= models.CharField(max_length=255)
     experience= models.CharField(max_length=255)
    #  content= models.TextField()
     timeStamp=models.DateTimeField(auto_now_add=True, blank=True)

     def __str__(self):
          return "Message from " + self.name + ' - ' + self.email