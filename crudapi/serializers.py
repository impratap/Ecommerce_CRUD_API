from rest_framework import serializers
from .models import Category, Book, Product, Cart
from django.contrib.auth.models import User

''' Serializers translates data into a format that is easy to consume over the internet, typically
JSON, and is displayed at an API endpoint.
'''

# Below I Have created reqired serializers


# This one for Category 
class CategorySerializer(serializers.ModelSerializer): # extended model serilaizer fort categorySerializer
    
    class Meta:  # created merta class and used fields and Model
        fields = (
            'id',
            'title'
        )
        model = Category 

# created BookSerializer for Book Model
class BookSerializer(serializers.ModelSerializer):
    created_by = serializers.ReadOnlyField(source='created_by.username', read_only=False)
    class Meta:
        fields = (
            'id',
            'title',
            'category',
            'author',
            'isbn',
            'pages',
            'price',
            'stock',
            'description',
            'imageUrl',
            'created_by',
            'status',
            'date_created'
        )
        model = Book

# Here Created ProductSerializer
class ProductSerializer(serializers.ModelSerializer):
    created_by = serializers.ReadOnlyField(source='created_by.username', read_only=False)
    class Meta:
        fields = (
            'id',
            'product_tag',
            'name',
            'category',
            'price',
            'stock',
            'imageUrl',
            'created_by',
            'status',
            'date_created'
        )
        model = Product

# CartUserSerializer
class CartUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('username', 'email')

# CartSerializer
class CartSerializer(serializers.ModelSerializer):

    cart_id = CartUserSerializer(read_only=True, many=False)
    books = BookSerializer(read_only=True, many=True)
    products = ProductSerializer(read_only=True, many=True)

    class Meta:
        model = Cart
        fields = ('cart_id', 'created_at', 'books', 'products')
