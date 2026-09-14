from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms


class TechnicianAccountForm(UserCreationForm):

    email = forms.EmailField()
    name = forms.CharField(max_length=100)
    phone = forms.CharField(max_length=15)
    specialization = forms.CharField(max_length=100)

    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'password1',
            'password2',
            'name',
            'phone',
            'specialization'
        ]