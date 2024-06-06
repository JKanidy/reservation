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
    computer_id = Computers.objects.get(id=computer_name)
    user = request.user
    reservation = Reservations.objects.filter(user_id=user, computer_id=computer_id)

    if not reservation.exists() and not Reservations.objects.filter(computer_id=computer_id).exists():
        Reservations.objects.create(user_id=request.user, computer_id=computer_id)
        alert = f"Вы успешно забронировали компьютер №{computer_id}"
    else:
        alert = "Компьютер уже забронирован"


    context = {
        'has_reservation': True,
        'alert_message': alert,
    }

    return render(request, 'products/products.html', context)


def reserve_delete(request):
    if request.method == 'POST':
        computer_id = request.POST.get('computer_id')
        user = request.user
        reservation = Reservations.objects.filter(user_id=user, computer_id=computer_id).first()

        if reservation:
            reservation.delete()

        alert2 = f"Вы отменили бронь компьютера №{computer_id}"

        context = {
            'has_reservation': True,
            'alert_message2': alert2,
        }

    return render(request, 'products/products.html', context)

