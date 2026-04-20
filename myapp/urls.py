from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import ListView
from . import views
from .models import Dreamreal
from .feeds import DreamrealCommentsFeed

urlpatterns = [
    # HOME
    path('', views.index),

    # BASIC
    path('hello/', views.hello),
    path('hello/<str:name>/', views.hello, name='hello'),

    # ARTIKEL
    path('artikel/<int:id>/', views.artikel),
    path('tambah/', views.tambah_artikel),
    path('daftar/', views.daftar_artikel, name='daftar'),
    path('edit/<int:id>/', views.edit_artikel),
    path('hapus/<int:id>/', views.hapus_artikel),
    path('articles/<int:year>/<int:month>/', views.viewArticles),

    # EMPLOYEE
    path('crud-emp/', views.crud_employee),
    path('add-emp/', views.add_employee),
    path('add-form/', views.add_employee_form),
    path('update-emp/<int:pk>/', views.update_employee, name='update_employee'),
    path('delete-emp/<int:pk>/', views.delete_employee, name='delete_employee'),

    # EMAIL
    path('send-email/', views.sendSimpleEmail),

    # STATIC
    path('static/', views.StaticView.as_view()),

    # LIST VIEW
    path('dreamreals/', ListView.as_view(
        model=Dreamreal,
        template_name="dreamreal_list.html"
    )),

    # AUTH
    path('login/', views.login_view, name='login'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('logout/', views.logout_view, name='logout'),
    
    # RSS FEED
    path('latest/comments/', DreamrealCommentsFeed(), name='rss_feed'),

    # DETAIL COMMENT
    path('comment/<int:pk>/', views.comment, name='comment'),


]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)