from django.shortcuts import render
from .models import Product
from django.http import JsonResponse
from django.forms.models import model_to_dict
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import ProductSerializer

@api_view(['GET'])
def api_view(request):
    query = Product.objects.all().order_by('?').first()
    data = {}
    if query:
        # data['name'] = query.name
        # data['content'] = query.content
        # data['price'] = query.price
        # data = model_to_dict(query, fields=('name', 'price', 'content', 'get_discount'))
        data=ProductSerializer(query).data
    return Response(data)