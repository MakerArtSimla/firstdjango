from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def project_list(request):
    return render(request, 'portfolio/project_list.html')

def home(request):
    return render(request, 'portfolio/index.html')
    # return HttpResponse("Welcome to my Portfolio!")
