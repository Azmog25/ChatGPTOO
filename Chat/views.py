from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home.html')

def resources(request):
    return render(request, 'ressource.html')

def conseils(request):
    return render(request, 'conseil.html')

def geri(request):
    return render(request, 'chat.html')
