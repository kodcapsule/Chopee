from django.urls import path
from . import views

urlpatterns = [
    path('', views.userCustomer , name='customer_page'),
]
