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
        'reservations': Reservations.objects.all(),
    }
    return render(request, 'products/products.html', context)

def reserve_computer(request, computer_name):
    computer = Computers.objects.get(id=computer_name)
    reservation = Reservations.objects.filter(user_id=request.user, computer_id=computer)

    if not reservation.exists():
        Reservations.objects.create(user_id=request.user, computer_id=computer)
    #else:
    #Написать, что уже забронирован пк
    return HttpResponseRedirect(request.META['HTTP_REFERER'])