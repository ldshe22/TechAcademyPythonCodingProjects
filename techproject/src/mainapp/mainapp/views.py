from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    # variable is products
    products = ["cherries", "apples", "oranges", "strawberries", "pears", "watermelons"]
    context = {
        'products': products,
    }
    return render(request, "home.html", context)
