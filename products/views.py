from django.shortcuts import render

# Create your views here.
def index(request):
    context = {'title': 'test1',
               'username': 'jora',
               }
    return render(request, 'products/index.html', context)

def products(request):
    return render(request, 'products/products.html')

def cabinet(request):
    return render(request, 'products/cabinet.html')