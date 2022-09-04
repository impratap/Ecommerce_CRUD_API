from django.contrib import admin
from .models import Category, Book, Product, Cart
# Register your models here.

admin.site.register(Category)
admin.site.register(Book)
admin.site.register(Product)
admin.site.register(Cart)

''' In the admin.py file we register all Model created in model.py file so that we casn use them if we don't do this
then we will not able to see this on admin panel and won't able to add data.'''