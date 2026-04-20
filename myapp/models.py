from django.db import models
from django.db import models
from django.db import models
from django.db import models
from django.db import models


class Artikel(models.Model):
    judul = models.CharField(max_length=200)
    isi = models.TextField()

    def __str__(self):
        return self.judul

    class Meta:
        db_table = "artikel"



class Employee(models.Model):
    empno = models.CharField(max_length=20)
    empname = models.CharField(max_length=100)
    alamat = models.CharField(max_length=100, null=True)
    salary = models.IntegerField()
    joined_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.empname} ({self.empno})"

    class Meta:
        db_table = "employee"

class Dreamreal(models.Model):
    name = models.CharField(max_length=100)

class Profile(models.Model):
    name = models.CharField(max_length=50)
    picture = models.ImageField(upload_to='pictures')

    class Meta:
        db_table = "profile"

class Comment(models.Model):
    dreamreal = models.ForeignKey(Dreamreal, on_delete=models.CASCADE)
    nama = models.CharField(max_length=100)
    isi = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nama

class Comment(models.Model):
    user_name = models.CharField(max_length=100)
    comment = models.TextField()
    submit_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user_name