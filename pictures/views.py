from django.shortcuts import render
from django.http  import HttpResponse, Http404
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from pictures.models import Post, Category, Author
from django import template
from django.db import models


def search_results(request):

    if 'post' in request.GET and request.GET["post"]:
        search_term = request.GET.get("post")
        searched_posts = Post.search_by_category(search_term)
        message = f"{search_term}"

        return render(request, 'pictures/search.html',{"message":message,"posts": searched_posts})

    else:
        message = "Ooops we can't find that!!"
        return render(request, 'pictures/search.html',{"message":message})

def viewPhoto(request, pk):
    post = Post.objects.get(id=pk)
    return render(request, 'pictures/image.html', {'post':post})


class ImageList(ListView):
    model = Post

def gallery(request):
    category= category.request.GET.get('category')
    print('category:', category)
    categories = Category.objects.all()
    authors = Author.objects.all()
    photos = Photo.objects.all()

    context = {'categories': categories,'photos':photos}

    return render(request, 'pictures/post_list.html', context)


class ImageCreate(CreateView):
    model = Post
    fields = ['image', 'imagename', 'description', 'author', 'category', 'location']
    success_url = '/'

# register = template.Library()
# Post = models.get_model('photologue', 'photo')

# def photo_url(format_string):
#     """Tries to load the appropriate Photologue Photo object by slug, and outputs
#        the url to the display image.  If photo is not found, then returns an empty
#        string."""
#     try:
#         photo = Photo.objects.get(title_slug=format_string, is_public=True)
#         return photo.get_display_url()
#     except Photo.DoesNotExist:
#         return ''

# register.simple_tag(photo_url)