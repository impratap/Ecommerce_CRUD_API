from django.shortcuts import render 
from rest_framework import generics, permissions 
from .models import Category, Book, Product, Cart
from .serializers import CategorySerializer, BookSerializer, ProductSerializer, CartSerializer

# Category view
class ListCategory(generics.ListCreateAPIView): # This is generics class view for list creation
    permission_classes = (permissions.IsAuthenticated,) # This is for permission so only login user can create
    queryset = Category.objects.all() # This is query to get the data from selected model
    serializer_class = CategorySerializer # And this is serializer it is used to covert data into jason format

class DetailCategory(generics.RetrieveUpdateDestroyAPIView): # This is for read, update and delete rest of CRUD operation
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


# Book View
class ListBook(generics.ListCreateAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class DetailBook(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Book.objects.all()
    serializer_class = BookSerializer

# Product Views
class ListProduct(generics.ListCreateAPIView):    
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class DetailProduct(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

# Cart View
class ListCart(generics.ListCreateAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Cart.objects.all()
    serializer_class = CartSerializer

class DetailCart(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Cart.objects.all()
    serializer_class = CartSerializer