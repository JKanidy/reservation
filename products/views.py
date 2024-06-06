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

    if not reservation.exists() and not Reservations.objects.filter(computer_id=computer).exists():
        Reservations.objects.create(user_id=request.user, computer_id=computer)

    return HttpResponseRedirect(request.META['HTTP_REFERER'])


def reserve_delete(request):
    if request.method == 'POST':
        computer_id = request.POST.get('computer_id')
        reservation = Reservations.objects.filter(user_id=request.user, computer_id=computer_id).first()

        if reservation:
            reservation.delete()

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
