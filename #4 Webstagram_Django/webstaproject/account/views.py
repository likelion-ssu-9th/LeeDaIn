from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def login_view(request):
    if request.method == 'POST':
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request=request, username=username, password=password)
        if user is not None:
            login(request, user)
        return redirect("base")
    else:
        return render(request, 'login.html')

def logout_view(request):
    logout(request)
    return redirect("base")

def signup(request):
    if request.method == 'POST':
            user = User.objects.create_user(
                username=request.POST["username"], password=request.POST["password"], first_name=request.POST["name"], last_name=request.POST["nickname"]
            )
            login(request, user)
            return redirect("base")
    else:
        return render(request, 'signup.html')