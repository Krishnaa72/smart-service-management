from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.admin.views.decorators import staff_member_required
from service.models import Technician
from .forms import TechnicianAccountForm


def user_login(request):

    if request.method == 'POST':

        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:
            login(request, user)
            return redirect('technician_list')

        content = {
            'error': 'Invalid username or password.'
        }

        return render(request, 'accounts/login.html', content)

    return render(request, 'accounts/login.html')

def user_logout(request):
    logout(request)
    return redirect('login')

@staff_member_required
def technician_create(request):

    if request.method == 'POST':

        form = TechnicianAccountForm(request.POST)

        if form.is_valid():

            user = form.save()

            Technician.objects.create(
                user=user,
                name=form.cleaned_data['name'],
                phone=form.cleaned_data['phone'],
                specialization=form.cleaned_data['specialization']
            )

            return redirect('technician_list')

    else:
        form = TechnicianAccountForm()

    content = {
        'form': form
    }

    return render(request, 'accounts/technician_form.html', content)
