from django.urls import path
from .views import daftar_artikel, edit_artikel, hapus_artikel, index, hello, artikel, tambah_artikel
from . import views
from .views import update_employee
from . import views
from myapp import views
from .views import StaticView
from django.views.generic import ListView
from .models import Dreamreal
from django.views.generic import TemplateView
from . import views
from .views import login_view
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns =[
    
    path('', index),
    path('hello/', hello),
    path('crud-emp/', views.crud_employee),
    path('artikel/<int:id>/', artikel),
    path('tambah/', tambah_artikel),
     path('daftar/', daftar_artikel),
    path('edit/<int:id>/', edit_artikel),
    path('hapus/<int:id>/', hapus_artikel),
    path("add-emp/", views.add_employee),
    path("add-form/", views.add_employee_form),
    path("update-emp/<int:pk>/", views.update_employee, name="update_employee"),
    path("delete-emp/<int:pk>/", views.delete_employee, name="delete_employee"),
    path('daftar/', views.daftar_artikel, name='daftar'),
    path('send-email/', views.sendSimpleEmail),
    path('static/', StaticView.as_view()),
    path('dreamreals/', ListView.as_view(
        model=Dreamreal,
        template_name="dreamreal_list.html"
    )),
    path('connection/', TemplateView.as_view(template_name='login.html')),
    path('login/', views.login, name='login'),
    path("login/", login_view, name="login"),
    path('profile/', views.save_profile, name='profile'),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)