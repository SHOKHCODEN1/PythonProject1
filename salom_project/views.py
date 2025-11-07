
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def Respublika(request):
    return HttpResponse("O'zbekiston Respublikasi")

def Mamlakat_viloyat(request):
    return HttpResponse("O'zbekiston Respublikasi Surxondaryo viloyati")

def mamlakat_viloyat_shahar(request):
    return HttpResponse("O'zbekiston Respublikasi Surxondaryo viloyati Termiz shahri")

def mamlakat_viloyat_shahar_akademiya(request):
    return HttpResponse("O'zbekiston Respublikasi Surxondaryo viloyati Termiz shahri Joylinks akademiyasi")