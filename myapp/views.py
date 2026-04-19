from django.shortcuts import render, redirect
from django.http import HttpResponse
import datetime

from myapp.forms import EmployeeForm
from .models import Artikel, Employee
from .models import Employee
from django.http import HttpResponse


# =========================
# HALAMAN UTAMA
# =========================
def index(request):
    return render(request, 'myapp/index.html')


# =========================
# HALAMAN HELLO
# =========================
def hello(request):
    today = datetime.date.today()
    days_of_week = ['Senin', 'Selasa', 'Rabu', 'Kamis', 'Jumat', 'Sabtu', 'Minggu']

    return render(request, 'myapp/hello.html', {
        'today': today,
        'days_of_week': days_of_week
    })


# =========================
# ARTIKEL (CRUD)
# =========================

def artikel(request, id):
    return HttpResponse(f"Artikel ke {id}")

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


# =========================
# EMPLOYEE (CRUD SIMPLE / TEST)
# =========================

def add_employee(request):
    emp = Employee(
        empno="E003",
        empname="Andi",
        contact="0815",
        salary=6000000
    )
    emp.save()

    return HttpResponse("Data Employee berhasil ditambahkan")


def crud_employee(request):

    # CREATE (contoh dummy)
    emp = Employee(
        empno="E001",
        empname="Budi",
        contact="0812",
        salary=5000000
    )
    emp.save()

    # READ ALL
    data = Employee.objects.all()
    res = "DATA EMPLOYEE:<br>"

    for e in data:
        res += f"{e.empname} - {e.empno}<br>"

    # UPDATE
    emp = Employee.objects.get(empno="E001")
    emp.salary = 7000000
    emp.save()

    # DELETE (opsional)
    # emp.delete()

    return HttpResponse(res)

def add_employee_form(request):
    if request.method == "POST":
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("Berhasil ditambah")

    else:
        form = EmployeeForm()

    return render(request, "myform.html", {"form": form})

def update_employee(request, pk):
    emp = Employee.objects.get(pk=pk)

    if request.method == "POST":
        emp.empname = request.POST['empname']
        emp.contact = request.POST['contact']
        emp.salary = request.POST['salary']
        emp.save()
        return HttpResponse("Update Employee berhasil!")

    return render(request, "myapp/update_employee.html", {"emp": emp})

def delete_employee(request, pk):
    emp = Employee.objects.get(pk=pk)
    emp.delete()
    return HttpResponse("Employee berhasil dihapus")