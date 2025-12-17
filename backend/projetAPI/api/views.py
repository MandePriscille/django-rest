from django.shortcuts import render
from django.http import JsonResponse

def api_view(request, *args, **kwargs):
    data = {
        'name': 'Priscille',
        'age': 25,
        'city': 'Paris',
        'language': 'French'
    }
    return JsonResponse(data)