from django.urls import path
from . import views

urlpatterns = [
    path('customers/', views.customer_list, name='customer_list'),
    path('customers/add/', views.customer_create, name='customer_create'),
    path('customers/<int:id>/', views.customer_detail, name='customer_detail'),
    path('customers/<int:id>/edit/', views.customer_update, name='customer_update'),
    path('customers/<int:id>/delete/', views.customer_delete, name='customer_delete'),
    
    path('service-requests/', views.service_request_list, name='service_request_list'),
    path('service-requests/add/', views.service_request_create, name='service_request_create'),
    path('service-requests/<int:id>/', views.service_request_detail, name='service_request_detail'),
    path('service-requests/<int:id>/edit/', views.service_request_update, name='service_request_update'),
    path('service-requests/<int:id>/delete/', views.service_request_delete, name='service_request_delete'),
]