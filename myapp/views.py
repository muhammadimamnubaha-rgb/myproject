from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Comment
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from django.views.decorators.cache import cache_page

from .models import Artikel, Employee, Dreamreal, Comment
from .forms import LoginForm, ArtikelForm, EmployeeForm, CommentForm


# ======================
# BASIC VIEW
# ======================

def index(request):
    return HttpResponse("Halaman Utama")


# ======================
# COMMENT + DREAMREAL
# ======================

def hello(request, name):
    dreamreal = get_object_or_404(Dreamreal, name=name)
    comments = Comment.objects.filter(dreamreal=dreamreal)

    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.dreamreal = dreamreal
            comment.save()
            return redirect('hello', name=name)
    else:
        form = CommentForm()

    return render(request, "hello.html", {
        "dreamreal": dreamreal,
        "comments": comments,
        "form": form
    })


# ======================
# COMMENT DETAIL (FIXED)
# ======================

def comment_detail(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    return HttpResponse(f"{comment.user_name} - {comment.comment}")

# ======================
# ARTIKEL CRUD
# ======================

@cache_page(60)
def daftar_artikel(request):
    data = Artikel.objects.all()
    return render(request, "daftar_artikel.html", {"data": data})


@cache_page(60)
def viewArticles(request, year, month):
    print("VIEW DIPANGGIL")
    return HttpResponse(f"Artikel bulan {month} tahun {year}")


def artikel(request, id):
    data = get_object_or_404(Artikel, id=id)
    return render(request, "detail_artikel.html", {"data": data})


def tambah_artikel(request):
    form = ArtikelForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('daftar')
    return render(request, "tambah_artikel.html", {"form": form})


def edit_artikel(request, id):
    data = get_object_or_404(Artikel, id=id)
    form = ArtikelForm(request.POST or None, instance=data)
    if form.is_valid():
        form.save()
        return redirect('daftar')
    return render(request, "edit_artikel.html", {"form": form})


def hapus_artikel(request, id):
    data = get_object_or_404(Artikel, id=id)
    data.delete()
    return redirect('daftar')


# ======================
# EMPLOYEE CRUD
# ======================

def crud_employee(request):
    data = Employee.objects.all()
    return render(request, "crud_employee.html", {"data": data})


def add_employee(request):
    form = EmployeeForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('crud_employee')
    return render(request, "add_employee.html", {"form": form})


def add_employee_form(request):
    return render(request, "add_employee_form.html")


def update_employee(request, pk):
    data = get_object_or_404(Employee, pk=pk)
    form = EmployeeForm(request.POST or None, instance=data)
    if form.is_valid():
        form.save()
        return redirect('crud_employee')
    return render(request, "update_employee.html", {"form": form})


def delete_employee(request, pk):
    data = get_object_or_404(Employee, pk=pk)
    data.delete()
    return redirect('crud_employee')


# ======================
# EMAIL (DUMMY)
# ======================

def sendSimpleEmail(request):
    return HttpResponse("Email berhasil dikirim (dummy)")


# ======================
# STATIC PAGE
# ======================

class StaticView(TemplateView):
    template_name = "static.html"


# ======================
# AUTH SYSTEM
# ======================

def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user:
            login(request, user)
            return redirect('dashboard')
        else:
            return render(request, "login.html", {
                "error": "Username / password salah"
            })

    return render(request, "login.html")


@login_required
@cache_page(30)
def dashboard(request):
    return render(request, "success.html", {
        "username": request.user.username
    })


def logout_view(request):
    logout(request)
    return redirect('login')

def comment_detail(request, pk):
    comment = get_object_or_404(Comment, pk=pk)

    return HttpResponse(f"""
        <h3>User:</h3> {comment.user_name} <br>
        <h3>Comment:</h3> {comment.comment}
    """)

def comment(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    return HttpResponse(f"{comment.user_name} - {comment.comment}")