from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from app.models import Bolo
from app.forms import CadastroForm


def index(request):
    bolos = Bolo.objects.all()
    return render(request, "index.html", {"bolos": bolos})


def logout_page(request):
    logout(request)
    return redirect(index)


def cadastro(request):
    form = CadastroForm()
    if request.method == "POST":
        form = CadastroForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            login(request, user)
            return redirect(index)
        else:
            return render(request, "registration/signup.html", {"form": form})
    return render(request, "registration/signup.html", {"form": form})
