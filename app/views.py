from .models import *
from django.shortcuts import render, redirect



# auth 

def index(request):
    return render(request, 'index.html')