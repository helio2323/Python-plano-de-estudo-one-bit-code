from django.shortcuts import render, redirect
from django.http import HttpResponse
import requests
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Create your views here.
def home(request):
    #return HttpResponse("My Home")
    if request.method == 'POST':
        username = request.POST.get('usuario')
        password = request.POST.get('senha')
        #Autenticação
        user = authenticate(
            request,
            username=username,
            password=password
        )
        if user is not None:
            resp = login(request, user)
            messages.success(
                request,
                "Login realizado com sucesso"
            )
            print(request.user)
            return redirect('home')
        else:
            messages.error(
                request,
                "Usuário ou senha inválidos"
            )
            return redirect('home')

    else:
        return render(request, 'home.html')

def logout_user(request):
    logout(request)
    messages.success(
        request,
        "Logout efetuado com sucesso"
    )
    return redirect('home')

def register_user(request):
    return render(request, 'register.html')