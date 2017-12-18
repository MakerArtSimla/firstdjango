from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'index.html')

# In alphabetical order from here onwards
def about(request):
    return render(request, 'about.html')
