from rest_framework import serializers
from .models import Product
from .validators import validate_product_name

class ProductSerializer(serializers.ModelSerializer):
    my_discount = serializers.SerializerMethodField(read_only=True)
    email = serializers.EmailField(write_only=True)
    name = serializers.CharField(validators=[validate_product_name])
    class Meta:
        model = Product
        fields = ('email', 'pk', 'name', 'content', 'price', 'my_discount')

    def create(self, validated_data):
        email = validated_data.pop('email')
        obj = super().create(validated_data)
        return obj

    def get_my_discount(self, obj):
        if not hasattr(obj, 'id'):
            return None
        if not isinstance(obj, Product):
            return None
        return obj.get_discount
    
    