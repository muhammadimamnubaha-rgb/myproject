from django.shortcuts import render
from django.http import HttpResponse
import datetime

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