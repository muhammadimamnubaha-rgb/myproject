from django.db import models

class Artikel(models.Model):
    judul = models.CharField(max_length=200)
    isi = models.TextField()

    def __str__(self):
        return self.judul