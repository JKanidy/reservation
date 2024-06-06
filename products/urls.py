from django.urls import path
from products.views import products, reserve_computer, reserve_delete

app_name = 'products'

urlpatterns = [
    path('', products, name='index'),
    path('computers_list/<int:computer_name>/', reserve_computer, name='reserve_computer'),
    path('computers_list/', reserve_delete, name='reserve_delete'),
]
