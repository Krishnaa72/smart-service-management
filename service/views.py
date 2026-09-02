from django.shortcuts import render
from . models import Customer

def customer_list(request):
    customers = Customer.objects.all()

    content = {
        'customers': customers
    }

    return render(request, 'service/customer_list.html', content)