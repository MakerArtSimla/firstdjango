# from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    # return render(request, 'index.html')
    return HttpResponse("Welcome to my Home Page!")

# In alphabetical order from here onwards
def about(request):
    return HttpResponse("WIt's all about me... :-)")
