from django.shortcuts import render
from .models import Author, Category, Location, Photo

# Create your views here.
def gallery(request):
    categories = Category.objects.all()
    authors = Author.objects.all()
    locations = Location.objects.all()
    photos = Photo.objects.all()
    context = {'categories': categories, 'authors': authors, 'locations':locations, 'photos':photos}
    return render(request, 'photos/gallery.html', context)

def viewPhoto(request, pk):
    photo = Photo.objects.get(id=pk)
    return render(request, 'photos/photo.html', {'photo':photo})

def newPhoto(request):
    return render(request, 'photos/new.html')