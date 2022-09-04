from django.urls import path
from .views import ListCategory, DetailCategory, ListBook, DetailBook, ListProduct, DetailProduct, ListCart, DetailCart

'''Here we are going to create the urls for the views which we have created in the views.py files.
for the different views we have to create specific url so that when the client request for paricular view server can 
respond with proper view. 

Our URLpattern has three parts:
* a Python regular expression for the empty string '' or with any word
* a reference to the view called like ListCategory
* an optional named URL pattern'''

urlpatterns = [
    path('categories', ListCategory.as_view(), name='categorie'),
    path('categories/<int:pk>/', DetailCategory.as_view(), name='singlecategory'),
    
    path('books', ListBook.as_view(), name='books'),
    path('books/<int:pk>/', DetailBook.as_view(), name='singlebook'),

    path('products', ListProduct.as_view(), name='products'),
    path('products/<int:pk>/', DetailProduct.as_view(), name='singleproduct'),

    path('carts', ListCart.as_view(), name='allcarts'),
    path('carts/<int:pk>', DetailCart.as_view(), name='cartdetail'),

]