from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Author(models.Model):
    first_name = models.CharField(max_length =30)
    last_name = models.CharField(max_length =30)
    email = models.EmailField()
    phone_number = models.CharField(max_length = 10,blank =True)

    def __str__(self):
        return self.last_name
    class Meta:
        ordering = ['last_name']  
        
class Category(models.Model):
    category = models.CharField(max_length =30, null='False', blank='False')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    
    def save_category(self):
        self.save()

    def __str__(self):
        return self.category

class Location(models.Model):
    country =  models.CharField(max_length =10)
    city =  models.CharField(max_length =10)
    
    def __str__(self):
        return self.city

    @classmethod
    def get_location_id(cls):
        location = Location.objects.all()
        return location


class Post(models.Model):
    image = models.ImageField(upload_to = 'articles/',default='IMAGE')
    imagename =  models.CharField(max_length =30)
    description = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    location = models.ForeignKey(Location, on_delete=models.CASCADE,default='LOCATION')

    def __str__(self):
        return self.imagename

    def save_post(self):
        self.save()

    @classmethod
    def search_by_category(cls,search_term):
        pictures = cls.objects.filter(category__category__icontains=search_term)
        return pictures



