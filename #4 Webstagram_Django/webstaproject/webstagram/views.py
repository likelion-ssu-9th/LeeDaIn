from django.shortcuts import redirect, render, get_object_or_404
from .models import Post
from .forms import PostForm
from django.contrib.auth.models import User

# Create your views here.
def base(request):
    return render(request, "base.html")

def feed(request):
    posts = Post.objects.all()
    return render(request, 'feed.html', {"posts" : posts})

def profile(request, id):
    writer = get_object_or_404(User, pk=id)
    posts = writer.post.all()
    return render(request, 'profile.html', {"writer" : writer, "posts" : posts})

def detail(request, id):
    post = get_object_or_404(Post, pk=id)
    return render(request, 'detail.html', {"post" : post})

def new(request):
    form = PostForm()
    return render(request, 'new.html', {'form' : form})

def create(request):
    form = PostForm(request.POST, request.FILES)
    if form.is_valid():
        new_post = form.save(commit=False)
        new_post.writer = request.user
        new_post.save()
        return redirect('detail', new_post.id)
    return redirect('base')

def edit(request, id):
    edit_post = Post.objects.get(id=id)
    return render(request, 'edit.html', {'edit_post' : edit_post})

def update(request, id): 
    update_post = get_object_or_404(Post, pk = id)
    update_post.image = request.FILE['image']
    return redirect('feed', update_post.id)

def delete(request, id):
    delete_post = Post.objects.get(id=id)
    delete_post.delete()
    return redirect('base')