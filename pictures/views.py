from django.shortcuts import render
from django.http  import HttpResponse, Http404
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from pictures.models import Post, Category, Author


def search_results(request):

    if 'post' in request.GET and request.GET["post"]:
        search_term = request.GET.get("post")
        searched_posts = Post.search_by_imagename(search_term)
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

class ImageCreate(CreateView):
    model = Post
    fields = ['image', 'imagename', 'description', 'author', 'category']
    success_url = '/'