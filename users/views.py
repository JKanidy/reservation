from django.shortcuts import render

# Create your views here.
def login(request):
    context = {'title': 'Вход',
               }
    return render(request, 'users/login.html', context)

def registration(request):
    context = {'title': 'Регистрация',
               }
    return render(request, 'users/registration.html', context)

def cabinet(request):
    context = {'title': 'Личный кабинет',
               }
    return render(request, 'users/cabinet.html', context)