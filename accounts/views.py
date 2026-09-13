from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect


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