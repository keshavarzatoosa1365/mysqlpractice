from django.db import models

class profile(models.Model):
    first_name=models.CharField(max_length=20,verbose_name="نام")    
    last_name=models.CharField(max_length=20,verbose_name="فامیل")    
   
