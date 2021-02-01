from django.shortcuts import render

from mainapp.models import Product, ProductCategory


# Create your views here.

def index(request):
    context = {
        'title': 'GeekShop',
    }
    return render(request, 'mainapp/index.html', context)


def products(request, id=None):
    if id:
        context = {
            'product': Product.objects.get(id=id)
        }
    else:
        context = {
            'title': 'Products',
            'products': Product.objects.all(),
            'categories': ProductCategory.objects.all(),
        }
    return render(request, 'mainapp/products.html', context)
