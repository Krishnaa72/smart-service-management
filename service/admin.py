from django.contrib import admin
from .models import Customer, ServiceRequest, ServiceCategory

admin.site.register(Customer)
admin.site.register(ServiceRequest)
admin.site.register(ServiceCategory)


