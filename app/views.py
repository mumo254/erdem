from app.forms import ReplyForm
from .models import *
from django.shortcuts import render, redirect



# auth      

def index(request):
    return render(request, 'index.html')

def blogs(request):
    posts = Blogs.objects.all()
    form = ReplyForm()
    if request.method == 'POST':  
        form = ReplyForm(request.POST, request.FILES)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.save()
            return redirect('blogs')
    print(posts)
    ctx= {
        "posts":posts,
        "form":form,
    }
    return render (request, 'blog.html', ctx )