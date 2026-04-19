from django.contrib import admin
from .models import Artikel, Employee


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ("empname", "empno", "alamat", "salary", "joined_date")
    search_fields = ("empname",)
    list_filter = ("joined_date",)


@admin.register(Artikel)
class ArtikelAdmin(admin.ModelAdmin):
    list_display = ("judul",)
    search_fields = ("judul",)