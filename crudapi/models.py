from django.db import models
from django.contrib.auth.models import User

# Create your models here.

''' Here creating a model for Category so that we can add different-different category for our items''' 

class Category(models.Model):
    title = models.CharField(max_length=200)


    def __str__(self): # This function is used to make object human and easy readable
        return self.title

''' Here creating Book model a new table so that we can can have a seperate table in database for book.
In this model we have used different-different datatype like we charfield, integerfield, urlfield, ForeignKey
Boolean and datefield. Foreign key is used to make many2one relation with another model or table in the database

'''

class Book(models.Model):
    title = models.CharField(max_length=200)
    category = models.ForeignKey(Category, related_name='books', on_delete=models.CASCADE)#This is many2one relation key
    author = models.CharField(max_length=100, default='Aryabhata')
    isbn = models.CharField(max_length=13)
    pages = models.IntegerField()
    price = models.IntegerField()
    stock = models.IntegerField() 
    description = models.TextField()
    imageUrl = models.URLField()
    created_by = models.ForeignKey('auth.User', related_name='books', on_delete=models.CASCADE)
    status = models.BooleanField(default=True)
    date_created = models.DateField(auto_now_add=True)

    
    '''Here I have created a Meta class, meta class is basically a inner class of model class
    it is used to change the behaviour of our model fields like changing order options,verbose_name'''
    
    class Meta:
        ordering = ['-date_created'] # This is for odering, used minus sign so that last created appear on the top.

    def __str__(self):
        return self.title

'''Here we are creating another model for Product so that we can add all product and store in this database'''

class Product(models.Model):
    product_tag = models.CharField(max_length=10)
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    price = models.IntegerField()
    stock = models.IntegerField()
    imageUrl = models.URLField()
    created_by = models.ForeignKey('auth.User', related_name='products', on_delete=models.CASCADE)
    status = models.BooleanField(default=True)
    date_created = models.DateField(auto_now_add=True)

    class Meta:
        ordering = ['-date_created']

    def __str__(self):
        return '{} {}'.format(self.product_tag, self.name) # using python string format function 

'''This is for cart when we select item from above tables or models than all item will added to this model
In this model we have used OneToOne and MnayToMany relational field'''

class Cart(models.Model):
    cart_id = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True)
    books = models.ManyToManyField(Book)
    products = models.ManyToManyField(Product)

    class Meta:
        ordering = ['cart_id', '-created_at']
        

    def __str__(self):
        return f'{self.cart_id}'