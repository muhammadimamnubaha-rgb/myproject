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