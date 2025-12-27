from .models import Product
from rest_framework import serializers

def validate_product_name(value):
    qs = Product.objects.filter(name__iexact=value)
    if qs.exists():
        raise serializers.ValidationError(f" Le produit {value} exist en base de donne")
    return value