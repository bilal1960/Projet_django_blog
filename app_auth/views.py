from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from django.contrib import messages

def login_blog(request):
    if request.method =="POST":
        username = request.POST['username']
        pwd = request.POST['pwd']
        user=authenticate(username=username,password=pwd)
        if user is not None:
            return redirect("home")
        else:
            messages.error(request,"Erreur d'authentification")
            return render(request, "login.html")
        
    return render(request,"login.html")
