
from .models import Product
from .serializers import ProductSerializer
from rest_framework import viewsets, mixins


class ProductViewset(viewsets.ModelViewSet):
    """
    Docstring for ProductViewset
    get -> list -> QuerySet
    post -> create
    put - > update
    path -> partial update
    delete -> destroy
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductListRetrive(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.RetrieveModelMixin):
    
    queryset= Product.objects.all()
    serializer_class = ProductSerializer

