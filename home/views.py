from django.shortcuts import render

# Create your views here.

def index(request):
    """dislays index.html page"""
    return render(request, "index.html")