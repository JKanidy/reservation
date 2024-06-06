from django.shortcuts import render, HttpResponseRedirect
from products.models import Computers, Reservations
from users.models import User

# Create your views here.
def index(request):
    context = {'title': 'Главная',
               }
    return render(request, 'products/index.html', context)

def products(request):
    context = {
        'title': 'Забронировать',
        'reservations': Reservations.objects.filter(user_id=request.user),
    }
    return render(request, 'products/products.html', context)

def reserve_computer(request, computer_name):
    computer = Computers.objects.get(id=computer_name)
    reservation = Reservations.objects.filter(user_id=request.user, computer_id=computer)

    if reservation.exists():
        computer_is_reserved = True
    else:
        computer_is_reserved = False

    context = {
        'computer_is_reserved': computer_is_reserved
    }
    return HttpResponseRedirect(request.META['HTTP_REFERER'])

def reserve_delete(request, reservation_id):
    reservation = Reservations.objects.filter(id=reservation_id)
    if reservation.exists():
        Reservations.objects.delete(id=reservation_id)
    return HttpResponseRedirect(request.META['HTTP_REFERER'])
