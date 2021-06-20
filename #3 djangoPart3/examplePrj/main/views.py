from django.shortcuts import render,get_object_or_404, redirect
from django.utils import timezone
from .models import Blog
from django.contrib.auth.models import User

def home(request):
    blogs= Blog.objects.all()
    return render(request,"home.html",{"blogs":blogs})

def new(request):
    return render(request,'new.html')

def create(request):
    new_blog=Blog()
    new_blog.title=request.POST['title']
    new_blog.body=request.POST['body']
    new_blog.pub_date= timezone.now()
    new_blog.author=request.user
    new_blog.save()
    return redirect('home')

def detail(request, blog_id) :
    blog=get_object_or_404(Blog, pk=blog_id)
    return render(request, 'detail.html', {"blog":blog})

def profile(request, author_id):
    author = get_object_or_404(User, pk=author_id)
    author_blogs = author.blog.all()
    return render(request, 'profile.html', {"author":author, "author_blogs":author_blogs})

