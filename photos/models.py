from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Author(models.Model):
    first_name = models.CharField(max_length =30,null='False', blank='False')
    last_name = models.CharField(max_length =30,null='False', blank='False')
    email = models.EmailField(null='False', blank='False')
    phone_number = models.CharField(max_length = 10,blank =True)

    def __str__(self):
        return self.last_name
    class Meta:
        ordering = ['last_name']  
        
class Category(models.Model):
    category = models.CharField(max_length =30, null='False', blank='False')
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    
    def __str__(self):
        return self.category
class Location(models.Model):
    country =  models.CharField(max_length =10)
    city =  models.CharField(max_length =10)
    
    def __str__(self):
        return self.city

class Photo(models.Model):
    image = models.ImageField(null='False', blank='False',upload_to = 'images/',default='IMAGE')
    imagename =  models.CharField(max_length =30)
    description = models.TextField(null='False', blank='False')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)

    def __str__(self):
        return self.description


