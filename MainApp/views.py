from django.shortcuts import get_object_or_404, render, redirect

# Create your views here.

def home(request):
    return render(request, 'index.html')

def search(request):
    return render(request, 'search.html')

def setprofile(request):
    return render(request, 'setprofile.html')

def themaselect(request):
    return render(request, 'themaselect.html')

def thema(request):
    return render(request, 'thema.html')

