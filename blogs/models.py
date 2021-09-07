from django.db import models
import datetime
import os

def filepath(request,filename):
    old_file_name = filename
    timenow= datetime.datetime.now().strftime('%Y%m%H%M%S')
    filename = "%s%s" ,(timenow,old_file_name)
    return os.path.join('uploads/',str(filename))

# Create your models here.
class Blogs(models.Model):
    article_header = models.CharField(max_length=60)
    article_description = models.CharField(max_length=300)
    article_banner = models.ImageField(blank=True,null=True)


    first_header = models.CharField(max_length = 40)
    first_description = models.CharField(max_length =300)
    first_image = models.ImageField(blank=True,null=True)

    
    second_header = models.CharField(max_length = 40)
    second_description = models.CharField(max_length =300)
    second_image = models.ImageField(blank=True,null=True)

    
    third_header = models.CharField(max_length = 40)
    third_description = models.CharField(max_length =300)
    third_image = models.ImageField(blank=True,null=True)

    
    fourth_header = models.CharField(max_length = 40)
    fourth_description = models.CharField(max_length =300)
    fourth_image = models.ImageField(blank=True,null=True)

    
    fifth_header = models.CharField(max_length = 40)
    fifth_description = models.CharField(max_length =300)
    fifth_image = models.ImageField(blank=True,null=True)

    
    sixth_header = models.CharField(max_length = 40)
    sixth_description = models.CharField(max_length =300)
    sixth_image = models.ImageField(blank=True,null=True)

    
    seventh_header = models.CharField(max_length = 40)
    seventh_description = models.CharField(max_length =300)
    seventh_image = models.ImageField(blank=True,null=True)

    
    eighth_header = models.CharField(max_length = 40)
    eighth_description = models.CharField(max_length =300)
    eighth_image = models.ImageField(blank=True,null=True)

    
    ninth_header = models.CharField(max_length = 40)
    ninth_description = models.CharField(max_length =300)
    ninth_image = models.ImageField(blank=True,null=True)

    
    tenth_header = models.CharField(max_length = 40)
    tenth_description = models.CharField(max_length =300)
    tenth_image = models.ImageField(blank=True,null=True)

    # def __str__(self) -> str:
    #     return self.article_header,self.article_description



    
class static_data(models.Model):
    background = models.ImageField(blank=True,null=True)    