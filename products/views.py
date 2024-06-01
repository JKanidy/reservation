from django.shortcuts import render

# Create your views here.
def index(request):
    context = {'title': 'Главная',
               }
    return render(request, 'products/index.html', context)

def products(request):
    context = {'title': 'Забронировать',
               }
    return render(request, 'products/products.html', context)

def cabinet(request):
    context = {'title': 'Личный кабинет',
               }
    return render(request, 'products/cabinet.html', context)