# from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def blogHome(request):
    # return render(request, 'blogHome.html')
    return HttpResponse("Welcome to My Journey!")

# In alphabetical order from here onwards
def blogPost(request):
    return HttpResponse("Here's the story of my journey through IT")
