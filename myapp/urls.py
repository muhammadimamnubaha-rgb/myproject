from django.urls import path
from .views import daftar_artikel, edit_artikel, hapus_artikel, index, hello, artikel, tambah_artikel

urlpatterns = [
    path('', index),
    path('hello/', hello),
    path('artikel/<int:id>/', artikel),
    path('tambah/', tambah_artikel),
     path('daftar/', daftar_artikel),
    path('edit/<int:id>/', edit_artikel),
    path('hapus/<int:id>/', hapus_artikel),
]