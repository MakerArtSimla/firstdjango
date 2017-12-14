from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return render(request, 'blog/index.html')
 # HttpResponse("Welcome to My Journey!")

# In alphabetical order from here onwards
def post(request):
    return HttpResponse("Here's my first post")
