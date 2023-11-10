from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError


def home(request):
    return render(request, "Home.html")

def signUp(request):
    if request.method == "GET":
        return render(request, "SignUp.html", {"form": UserCreationForm})
    else:
        if request.POST["password1"] == request.POST["password2"]:
            # Register user
            try:
                user = User.objects.create_user(
                    username=request.POST["username"],
                    password=request.POST["password1"],
                )
                user.save()
                login(request, user)
                return redirect("reservation")
            except IntegrityError:
                return render(
                    request,
                    "SignUp.html",
                    {"form": UserCreationForm, "error": "El usuario ya existe"},
                )
        else:
            return render(
                request,
                "SignUp.html",
                {"form": UserCreationForm, "error": "Las contraseñas no coinciden"},
            )

def reservation(request):
    return render(request, "Reservation.html")

def signOut(request):
    logout(request)
    return redirect("home")

def signIn(request):
    if request.method == "GET":
        return render(request, "SignIn.html", {"form":AuthenticationForm})
    else:
        user= authenticate(request, username=request.POST["username"], password=request.POST["password"])
        print(request.POST)
        if user is None:
            return render(request, "SignIn.html",{"form":AuthenticationForm, "error":"Usuario o Contraseña Incorrectos"})
        else:
            login(request, user)
            return redirect("reservation")

## Segundo parcial 
def Hoteles (request):
    return render (request, "Hoteles.html")

def Personal(request):
    return render(request, "Personal.html")

def Usuarios(request):
    return render(request, "Usuarios.html")