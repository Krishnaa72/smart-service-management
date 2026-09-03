from django.shortcuts import render, redirect, get_object_or_404
from . models import Customer
from . forms import CustomerForm

def customer_list(request):
    customers = Customer.objects.all()

    content = {
        'customers': customers
    }

    return render(request, 'service/customer_list.html', content)

def customer_create(request):

    if request.method == 'POST':
        form = CustomerForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('customer_list')

    else:
        form = CustomerForm()

    content = {
        'form': form
    }

    return render(request, 'service/customer_form.html', content)

def customer_detail(request, id):
    customer = get_object_or_404(Customer, id=id)

    content = {
        'customer': customer
    }

    return render(request, 'service/customer_detail.html', content)