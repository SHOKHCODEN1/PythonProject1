from django.http import HttpResponse
from django.shortcuts import render

from .models import BookModel

def home(request):
    html = """
    <ul>
        <li>/salom/ber/ ➡ Assalomu alaykum</li>
        <li>/mamlakat/ ➡ O'zbekiston Respublikasi</li>
        <li>/mamlakat/viloyat ➡ O'zbekiston Respublikasi Surxondaryo viloyati</li>
        <li>/mamlakat/viloyat/shahar ➡ O'zbekiston Respublikasi Surxondaryo viloyati Termiz shahri</li>
        <li>/mamlakat/viloyat/shahar/akademiya ➡ O'zbekiston Respublikasi Surxondaryo viloyati Termiz shahri Joylinks akademiyasi</li>
    </ul>
    """
    return HttpResponse(html)


def salom_ber(request):
    return HttpResponse("Assalomu alaykum")

def mamlakat(request):
    return HttpResponse("O'zbekiston Respublikasi")

def mamlakat_viloyat(request):
    return HttpResponse("O'zbekiston Respublikasi Surxondaryo viloyati")

def mamlakat_viloyat_shahar(request):
    return HttpResponse("O'zbekiston Respublikasi Surxondaryo viloyati Termiz shahri")

def mamlakat_viloyat_shahar_akademiya(request):
    return HttpResponse("O'zbekiston Respublikasi Surxondaryo viloyati Termiz shahri Joylinks akademiyasi")
def hamma_kitoblar(request):
    all_books = BookModel.objects.all()
    context = {
        'all_books':all_books
    }
    return render(request, 'asosiy_sahifa.html', context)


def kitob_detail(request , id):
    book = BookModel.objects.get(id=id)
    context = {
        'book':book
    }
    return render(request , 'kitob_detail.html' , context)
