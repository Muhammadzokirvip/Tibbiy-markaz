from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    """Asosiy sahifani ko'rish uchun"""
    return render(request, 'index.html')


def about(request):
    """Blog sahifani ko'rish uchun"""
    return render(request, 'about.html')


def services(request):
    """Xizmatlar sahifasini ko'rish uchun"""
    return render(request, 'services.html')


def contact(request):
    """Xabar qoldirish sahifasini ko'rish uchun"""
    return render(request, 'contact.html')