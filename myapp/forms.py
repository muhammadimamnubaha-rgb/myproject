from django import forms


class LoginForm(forms.Form):
    user = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput())


class EmployeeForm(forms.Form):
    empno = forms.CharField(max_length=20)
    empname = forms.CharField(max_length=100)
    contact = forms.CharField(max_length=15)
    salary = forms.IntegerField()

class ProfileForm(forms.Form):
    name = forms.CharField(max_length=100)
    picture = forms.ImageField()

from django import forms
from .models import Artikel, Employee

# LOGIN FORM
class LoginForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)

# ARTIKEL FORM
class ArtikelForm(forms.ModelForm):
    class Meta:
        model = Artikel
        fields = '__all__'

# EMPLOYEE FORM
class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = '__all__'

from django import forms
from .models import Comment

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['user_name', 'comment']