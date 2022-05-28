from django.shortcuts import render
from .models import Author, Category, Location, Photo

# Create your views here.
def gallery(request):
    return render(request, 'photos/gallery.html')

def viewPhoto(request, pk):
    return render(request, 'photos/photo.html')

def newPhoto(request):
    return render(request, 'photos/new.html')