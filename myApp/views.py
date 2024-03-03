from django.shortcuts import render
from .models import *

# Create your views here.
def anasayfa(request):
    urunler=Urunler.objects.all()
    context={
        'urunler':urunler
    }
    return render(request,"index.html",context)

def detay(request,id):
    urun=Urunler.objects.filter(id=id)
    context={
        "urun":urun
    }
    return render(request,"detay.html",context)