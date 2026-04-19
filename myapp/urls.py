from django.urls import path
from .views import daftar_artikel, edit_artikel, hapus_artikel, index, hello, artikel, tambah_artikel
from . import views
from .views import update_employee
from . import views


urlpatterns = [
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

]