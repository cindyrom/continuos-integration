from rest_framework import serializers
from .models import Product


class ProductSerializer(serializers.ModelSerializer):
    is_active = serializers.BooleanField(read_only=True)

    class Meta:
        model = Product
        fields = ('id', 'name', 'description', 'last_udpated_on', 'is_active')