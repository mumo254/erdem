from .models import *
from django.shortcuts import render, redirect



# auth      

def index(request):
    return render(request, 'index.html')

def blogs(request):
    posts = Blogs.objects.all()
    reply = 
    print(posts)
    ctx= {
        "posts":posts,
    }
    return render (request, 'blog.html', ctx )