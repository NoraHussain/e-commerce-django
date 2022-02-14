from ast import Pass
from itertools import product
from django.shortcuts import render
from .models import *


def products_list(request):

    products_list = Product.objects.all()
    context = {'products_list': products_list}

    return render(
        request,
        'website/product_list.html',
        context
    )


def product_details(request, slug):
    product_details = Product.objects.get(PRDSlug=slug)
    context = {'product_details': product_details}

    return render(
        request,
        'website/product_details.html',
        context
    )
