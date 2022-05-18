from app.forms import CommentForm, ReplyForm
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

def blogDetails(request,blogs_id):
    posts = Blogs.objects.all()
    form = ReplyForm()
    blog = Blogs.objects.filter(pk = blogs_id)
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
        "blog":blog,
    }
    return render (request, 'blog-details.html', ctx)

def blogDetail(request):
    posts = Blogs.objects.all()
    form = ReplyForm()
    blog = Blogs.objects.filter()
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
        "blog":blog,
    }
    return render (request, 'blog-details.html', ctx)

def comments(request, blogs_id):
  form = ReplyForm()
  post = Blogs.objects.filter(pk = blogs_id).first()
  if request.method == 'POST':
    form = ReplyForm(request.POST)
    if form.is_valid():
      comment = form.save(commit = False)
      comment.blog = post
      comment.save() 
  return redirect('blogDetail') 

def blogsDetails(request,blogs_id):
    posts = Blogs.objects.all()
    form = CommentForm()
    blog = Blogs.objects.filter(pk = blogs_id)
    if request.method == 'POST':  
        form = CommentForm(request.POST, request.FILES)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.save()
            return redirect('blogs')
    print(posts)
    ctx= {
        "posts":posts,
        "form":form,
        "blog":blog,
    }
    return render (request, 'blog-details.html', ctx)

def blogsDetail(request):
    posts = Blogs.objects.all()
    form = CommentForm()
    blog = Blogs.objects.filter()
    if request.method == 'POST':  
        form = CommentForm(request.POST, request.FILES)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.save()
            return redirect('blogs')
    print(posts)
    ctx= {
        "posts":posts,
        "form":form,
        "blog":blog,
    }
    return render (request, 'blog-details.html', ctx)

def comment(request, blogs_id):
  form = CommentForm()
  post = Blogs.objects.filter(pk = blogs_id).first()
  if request.method == 'POST':
    form = CommentForm(request.POST)
    if form.is_valid():
      comment = form.save(commit = False)
      comment.blog = post
      comment.save() 
  return redirect('blogsDetail') 

