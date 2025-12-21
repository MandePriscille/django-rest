from django.shortcuts import render
from .models import Product
from django.http import JsonResponse
from django.forms.models import model_to_dict
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import ProductSerializer
from rest_framework import generics, mixins

# @api_view(['POST'])
# def api_view(request):
#     # query = Product.objects.all().order_by('?').first()
#     # serializer = {}
#     serializer = ProductSerializer(data=request.data)
#     if serializer.is_valid(raise_exception=True):
#         serializer.save()
#         return Response(serializer.data)
#     else:
#         return Response({'details':"invalid data"})
    
    # data = request.data
    # if query:
        # data['name'] = query.name
        # data['content'] = query.content
        # data['price'] = query.price
        # data = model_to_dict(query, fields=('name', 'price', 'content', 'get_discount'))
        # data=ProductSerializer(query).data

     
    # return Response(data)


class DetailApiView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class CreateApiView(generics.CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    
    def perform_create(self, serializer):
        name = serializer.validated_data.get('name')
        content = serializer.validated_data.get('content', '') or None
        if content is None:
            content = name
        serializer.save(content=content)


class UpdateApiView(generics.UpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'

    def perform_update(self, serializer):
        name = serializer.validated_data.get('name')
        content = serializer.validated_data.get('content', '') or None
        if content is None:
            content = name
        serializer.save(content=content)
    

class DeleteApiView(generics.DestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'

class ListApiView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get_queryset(self):
        return super().get_queryset().filter(name="avocat")


class ProductMixinView(generics.GenericAPIView,
                       mixins.CreateModelMixin,
                       mixins.UpdateModelMixin,
                       mixins.ListModelMixin,
                       mixins.DestroyModelMixin):
    
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'

    def perform_create(self, serializer):
        name = serializer.validated_data.get('name')
        content = serializer.validated_data.get('content', '') or None
        if content is None:
            content = name
        serializer.save(content=content)

    def perform_update(self, serializer):
        name = serializer.validated_data.get('name')
        content = serializer.validated_data.get('content', '') or None
        if content is None:
            content = name
            serializer.save(content=content)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


    # def get_queryset(self):
    #     return super().get_queryset().filter(name="avocat")

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

    
    def get(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        if pk is None:
            # return self.retrieve(request, *args, **kwargs)
            pass
        return self.list(request, *args, **kwargs)
    
    
