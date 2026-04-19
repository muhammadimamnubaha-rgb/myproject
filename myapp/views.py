from django.shortcuts import render, redirect
from django.http import HttpResponse
import datetime
from .models import Artikel

def index(request):
    return render(request, 'myapp/index.html')

def hello(request):
    today = datetime.date.today()
    days_of_week = ['Senin', 'Selasa', 'Rabu', 'Kamis', 'Jumat', 'Sabtu', 'Minggu']

    return render(request, 'myapp/hello.html', {
        'today': today,
        'days_of_week': days_of_week
    })

def artikel(request, id):
    return HttpResponse(f"Artikel ke {id}")

# 🔥 TAMBAHAN BARU (CRUD)

def daftar_artikel(request):
    data = Artikel.objects.all()
    return render(request, 'myapp/artikel_list.html', {'data': data})

def tambah_artikel(request):
    if request.method == 'POST':
        judul = request.POST['judul']
        isi = request.POST['isi']
        Artikel.objects.create(judul=judul, isi=isi)
        return redirect('/daftar/')
    return render(request, 'myapp/tambah.html')

def edit_artikel(request, id):
    artikel = Artikel.objects.get(id=id)

    if request.method == 'POST':
        artikel.judul = request.POST['judul']
        artikel.isi = request.POST['isi']
        artikel.save()
        return redirect('/daftar/')

    return render(request, 'myapp/edit.html', {'artikel': artikel})

def hapus_artikel(request, id):
    artikel = Artikel.objects.get(id=id)
    artikel.delete()
    return redirect('/daftar/')