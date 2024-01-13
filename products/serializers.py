# make a serializer to our data representation
from rest_framework import serializers
from products.models import Products

# make a serializer class
class ProductSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=Products
        fields="__all__"