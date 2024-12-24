from rest_framework import serializers
from .models import User, Product, Purchase, Seller

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
        
class SellerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Seller
        fields = '__all__'
        
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'title', 'description', 'price', 'status', 'seller', 'for_sale']


class PurchaseSerializer(serializers.ModelSerializer):
    product = ProductSerializer()
    buyer = serializers.StringRelatedField() 
    seller = serializers.StringRelatedField()

    class Meta:
        model = Purchase
        fields = '__all__'

