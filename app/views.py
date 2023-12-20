from django.shortcuts import render
from app.models import Bolo


def index(request):
    bolos = Bolo.objects.all()
    return render(request, "index.html", {"bolos": bolos})
