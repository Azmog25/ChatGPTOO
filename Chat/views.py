from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home.html')

def resources(request):
    return render(request, 'templates/ressource.html')

def advice(request):
    return render(request, 'templates/conseil.html')

def chat(request):
    return render(request, 'templates/chat.html')
