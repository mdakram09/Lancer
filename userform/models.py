from django.db import models

# Create your models here.
class Userform(models.Model):
     sno= models.AutoField(primary_key=True)
     name= models.CharField(max_length=255)
     email= models.CharField(max_length=100)
     phone= models.CharField(max_length=13)
     state= models.CharField(max_length=100)
     city= models.CharField(max_length=100)
     road= models.CharField(max_length=100)
     building= models.CharField(max_length=100)
     pin= models.CharField(max_length=100)
     kindofwork= models.CharField(max_length=100,null=True)
     content= models.TextField()
     timeStamp=models.DateTimeField(auto_now_add=True, blank=True)

     def __str__(self):
          return "Message from " + self.name + ' - ' + self.email