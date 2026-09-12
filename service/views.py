from django.shortcuts import render, redirect, get_object_or_404
from .models import Customer, ServiceRequest, Technician
from . forms import CustomerForm, ServiceRequestForm

#-------------------------------CUSTOMER LIST--------------------------------------#

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

def customer_update(request, id):
    customer = get_object_or_404(Customer, id=id)

    if request.method == 'POST':
        form = CustomerForm(request.POST, instance=customer)

        if form.is_valid():
            form.save()
            return redirect('customer_detail', id=customer.id)

    else:
        form = CustomerForm(instance=customer)

    content = {
        'form': form,
        'customer': customer
    }

    return render(request, 'service/customer_form.html', content)

def customer_delete(request, id):
    customer = get_object_or_404(Customer, id=id)

    if request.method == 'POST':
        customer.delete()
        return redirect('customer_list')

    content = {
        'customer': customer
    }

    return render(request, 'service/customer_confirm_delete.html', content)

#-------------------------------SERVICE REQUEST--------------------------------------#

def service_request_list(request):
    service_requests = ServiceRequest.objects.select_related(
        'customer',
        'category',
        'technician'
    )

    content = {
        'service_requests': service_requests
    }

    return render(request, 'service/service_request_list.html', content)

def service_request_create(request):

    if request.method == 'POST':
        form = ServiceRequestForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('service_request_list')

    else:
        form = ServiceRequestForm()

    content = {
        'form': form
    }

    return render(request, 'service/service_request_form.html', content)

def service_request_detail(request, id):
    service_request = get_object_or_404(ServiceRequest, id=id)

    content = {
        'service_request': service_request
    }

    return render(request, 'service/service_request_detail.html', content)

def service_request_update(request, id):
    service_request = get_object_or_404(ServiceRequest, id=id)

    if request.method == 'POST':
        form = ServiceRequestForm(
            request.POST,
            instance=service_request
        )

        if form.is_valid():
            form.save()
            return redirect('service_request_detail', id=service_request.id)

    else:
        form = ServiceRequestForm(instance=service_request)

    content = {
        'form': form,
        'service_request': service_request
    }

    return render(request, 'service/service_request_form.html', content)

def service_request_delete(request, id):
    service_request = get_object_or_404(ServiceRequest, id=id)

    if request.method == 'POST':
        service_request.delete()
        return redirect('service_request_list')

    content = {
        'service_request': service_request
    }

    return render(request, 'service/service_request_confirm_delete.html', content)

def technician_requests(request, id):
    technician = get_object_or_404(Technician, id=id)
    service_requests = technician.service_requests.select_related('customer','category')

    content = {
        'technician': technician,
        'service_requests': service_requests
    }

    return render(request, 'service/technician_requests.html', content )

def technician_detail(request, id):
    technician = get_object_or_404(Technician, id=id)

    content = {
        'technician': technician
    }

    return render(request, 'service/technician_detail.html', content)

def technician_list(request):
    technicians = Technician.objects.all()

    content = {
        'technicians': technicians
    }

    return render(request, 'service/technician_list.html', content)