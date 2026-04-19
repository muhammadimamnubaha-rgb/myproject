from django.urls import path
from .views import index, hello, artikel

urlpatterns = [
    path('', index),
    path('hello/', hello),
    path('artikel/<int:id>/', artikel),
]