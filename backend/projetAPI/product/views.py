from django.shortcuts import render
from .models import Product
from django.http import JsonResponse

def api_view(request):
    query = Product.objects.all().order_by('?').first()
    data = {}
    if query:
        data['name'] = query.name
        data['content'] = query.content
        data['price'] = query.price

    return JsonResponse(data)