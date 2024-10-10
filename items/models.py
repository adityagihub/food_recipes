from django.db import models

# Create your models here.

    
    
class recipe2(models.Model):
    rname = models.CharField(max_length=100)
    rdes  = models.CharField(max_length=100)
    rprice = models.IntegerField()    
    img1 = models.FileField(upload_to='img_store/')