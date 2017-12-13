from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request, 'portfolio/index.html')
    # return HttpResponse("Welcome to my Portfolio!")

# In alphabetical order from here onwards
def addProject(request):
    return render(request, 'portfolio/project.html', {'projectName': request.GET['projectName']})
    # return HttpResponse("I see you want to add a new project named: " +
    #     request.GET['projectName'])


def project_list(request):
    # read project list from database
    return render(request, 'portfolio/project_list.html')


def saveProject(request):
    return HttpResponse("I see you want to save a project called: " + request.GET['projectName']
    + ", which is about: " + request.GET['projectDescription'])

#   save project to database
#       projectName
#       projectDescription
#   later on:
#       project images
