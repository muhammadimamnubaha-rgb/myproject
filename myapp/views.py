from django.shortcuts import render, redirect
from django.http import HttpResponse
import datetime
from .models import Dreamreal
from myapp.forms import EmployeeForm
from .models import Artikel, Employee
from .models import Employee
from django.http import HttpResponse
from django.core.mail import send_mail
from django.http import HttpResponse
from django.core.mail import send_mass_mail
from django.http import HttpResponse
from django.core.mail import mail_admins
from django.http import HttpResponse
from django.core.mail import mail_managers
from django.http import HttpResponse
from django.core.mail import EmailMessage
from django.http import HttpResponse
from django.core.mail import EmailMessage
from django.http import HttpResponse
from django.core.mail import send_mail
from django.http import HttpResponse
from django.views.generic import TemplateView
from django.shortcuts import render
from myapp.forms import LoginForm
from django.shortcuts import render, redirect
from .forms import LoginForm
from django.shortcuts import render
from .forms import ProfileForm
from .models import Profile

# =========================
# HALAMAN UTAMA
# =========================
def index(request):
    return render(request, 'myapp/index.html')

def hello(request):
    return redirect("https://www.djangoproject.com")

def viewArticle(request, articleId):
    return redirect("/daftar/")

def viewArticle(request, articleId):
    return redirect(viewArticles, year=2045, month=2)


def viewArticles(request, year, month):
    return HttpResponse(f"Artikel {year}/{month}")


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
        return redirect('daftar')
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
    emp = Employee.objects.filter(empno="E001").first()
    empno="E001",
    empname="Budi",
    contact="0812",
    salary=5000000
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

def sendSimpleEmail(request):
    res = send_mail(
        subject="Hello",
        message="Ini email dari Django",
        from_email="emailkamu@gmail.com",
        recipient_list=["tujuan@gmail.com"],
        fail_silently=False
    )
    return HttpResponse(f"Terkirim: {res}")

def sendMassEmail(request):
    msg1 = ('Subject 1', 'Isi email 1', 'emailkamu@gmail.com', ['a@gmail.com'])
    msg2 = ('Subject 2', 'Isi email 2', 'emailkamu@gmail.com', ['b@gmail.com'])

    res = send_mass_mail((msg1, msg2), fail_silently=False)
    return HttpResponse(f"Terkirim: {res}")

def sendAdminsEmail(request):
    res = mail_admins(
        subject="Warning",
        message="Website bermasalah"
    )
    return HttpResponse(f"Terkirim: {res}")

def sendManagersEmail(request):
    res = mail_managers(
        subject="Info Update",
        message="Ada update sistem"
    )
    return HttpResponse(f"Terkirim: {res}")

def sendHTMLEmail(request):
    html_content = "<h1>Hello</h1><p>Ini email HTML</p>"

    email = EmailMessage(
        "Subject HTML",
        html_content,
        "emailkamu@gmail.com",
        ["tujuan@gmail.com"]
    )

    email.content_subtype = "html"
    res = email.send()
    return HttpResponse(f"Terkirim: {res}")

def sendEmailWithAttach(request):
    email = EmailMessage(
        "Subject File",
        "Silakan lihat lampiran",
        "emailkamu@gmail.com",
        ["tujuan@gmail.com"]
    )

    file = open('manage.py', 'rb')
    email.attach('manage.py', file.read(), 'text/plain')

    res = email.send()
    return HttpResponse(f"Terkirim: {res}")

class StaticView(TemplateView):
    template_name = "static.html"

def login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        # CEK KOSONG
        if not username or not password:
                return render(request, "login.html", {"error": "Isi semua field!"})

        # LOGIN SEDERHANA
        if username == "admin" and password == "123":
                return render(request, "loggedin.html", {"username": username})
        else:
                return render(request, "login.html", {"error": "Username / password salah"})

    return render(request, "login.html")
def login_view(request):
    if request.method == "POST":
        form = LoginForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            # login sederhana (contoh manual)
            if username == "admin" and password == "123":
                return render(request, "success.html", {"username": username})
            else:
                return render(request, "login.html", {
                    "form": form,
                    "error": "Username / password salah"
                })

    else:
        form = LoginForm()

    return render(request, "login.html", {"form": form})

def save_profile(request):
    saved = False

    if request.method == "POST":
        form = ProfileForm(request.POST, request.FILES)

        if form.is_valid():
            profile = Profile()
            profile.name = form.cleaned_data["name"]
            profile.picture = form.cleaned_data["picture"]
            profile.save()
            saved = True

    else:
        form = ProfileForm()

    return render(request, "profile.html", {"form": form, "saved": saved})