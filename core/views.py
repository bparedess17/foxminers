from django.shortcuts import render, get_object_or_404
from .models import Helmet

def home(request):
    return render(request, "core/index.html")

def index(request):
    return render(request, "core/index.html")

def equipo(request):
    return render(request, "core/equipo.html")

def login_view(request):
    return render(request, "core/login.html")

def dashboard(request):
    casco = get_object_or_404(Helmet, name="Casco 1")
    lectura = casco.readings.first()  # por Meta.ordering es la más reciente
    ctx = {"helmet": casco, "reading": lectura}
    return render(request, "core/dashboard.html", ctx)
