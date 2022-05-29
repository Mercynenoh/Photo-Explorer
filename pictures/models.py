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

class Post(models.Model):
    image = models.ImageField(upload_to = 'articles/',default='IMAGE')
    imagename =  models.CharField(max_length =30)
    description = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    
    def __str__(self):
        return self.imagename

    def save_post(self):
        self.save()

    @classmethod
    def search_by_imagename(cls,search_term):
        object_list = cls.objects.filter(imagename__icontains=search_term)
        return object_list



