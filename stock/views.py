from django.shortcuts import render
from stock.models import Stock

# Create your views here.

def stock(request):
    items = Stock.objects.all()
    return render(request, "stock/stock.html", {"items": items})