from bbe.models import Product, ProductImage
from rest_framework import serializers


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = [
            "id",
            "price",
            "product_name",
            "product_description",
            "max_quantity",
            "is_available",
            "image",
        ]


class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = ["image"]
