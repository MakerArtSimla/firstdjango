from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Post
from django.core.exceptions import ObjectDoesNotExist

# Create your views here.

def home(request):
    posts = Post.objects.order_by('-publishDate')
    return render(request, 'blog/index.html', {'posts' : posts})

# In alphabetical order from here onwards
def post(request, post_id):
    post = get_object_or_404(Post,pk=post_id)
    # some very rough code for pagination from post to post
    nextId = post.id + 1
    try:
        Post.objects.get(pk=nextId)
    except ObjectDoesNotExist:
        nextId = post.id

    prevId = post.id - 1
    try:
        Post.objects.get(pk=prevId)
    except ObjectDoesNotExist:
        prevId = post_id

    return render(request, 'blog/post.html', {'post': post , 'nextId': nextId, 'prevId': prevId, } )
