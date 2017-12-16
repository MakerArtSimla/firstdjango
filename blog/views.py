from django.shortcuts import render
from django.http import HttpResponse
from .models import Post

# Create your views here.

def home(request):
    posts = Post.objects.order_by('publishDate')

    return render(request, 'blog/index.html', {'posts' : posts})

# In alphabetical order from here onwards
def post(request):
    post = request.GET()

    # return HttpResponse("Here's my first post")
    return render(request, 'blog/post.html', {'post': request.GET['post'] } )
