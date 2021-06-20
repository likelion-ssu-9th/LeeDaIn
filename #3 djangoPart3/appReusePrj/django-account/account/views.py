from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import auth

def signup(request):
    if request.method == "POST": 
        if request.POST["password1"]== request.POST["password2"]: #1차비번과 2차 비번이 같다면
            user=User.objects.create_user(username=request.POST["username"], #사용자를 등록
                                          password=request.POST["password1"])
            auth.login(request,user)
            return redirect('home') 
        return render(request, 'signup.html')   #비번이 같지 않다면 'signup.html'로
    else:
        return render(request, 'signup.html')

def login(request):
    if request.method=="POST" : #요청방식이 POST라면
        username= request.POST['username']
        password= request.POST['password']
        user=auth.authenticate(request, username=username, password=password)

        if user is not None: #해당하는 유저가 있다면
            auth.login(request, user) #로그인 시켜줘라
            return redirect('home')
        else: #해당하는 유저가 없다면 
            return render(request, 'login.html',{'error' : 'username or password is incorrect. '})
    else:
        return render(request, 'login.html')

def logout(request):
    auth.logout(request)
    return redirect('home')