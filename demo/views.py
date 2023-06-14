from django.shortcuts import render, get_object_or_404

from rest_framework.viewsets import ModelViewSet
from .models import Product
from .serializers import ProductSerializer


class ProductViewSet(ModelViewSet):
    serializer_class = ProductSerializer

    def get_object(self):
        return get_object_or_404(Product, id=self.request.query_params.get("id"))

    def get_queryset(self):
        return Product.objects.filter(is_active=True).order_by('-last_udpated_on')

    def perform_destroy(self, instance):
        instance.is_active = False
        instance.save()