from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Slider(models.Model):
    firstTitle = models.CharField(max_length=50)
    secTitle = models.CharField(max_length=50)
    paragraph = models.CharField(max_length=200)
    price = models.FloatField()
    discounted = models.FloatField()
    image = models.ImageField(null=True, blank=True)

    def __str__(self) :
        return self.secTitle

class Arrivals(models.Model):
    photo = models.ImageField(null=True, blank=True)
    price = models.FloatField(default=1)
    title = models.CharField(max_length=20)

    def __str__(self) :
        return self.title

class Featured(models.Model):
    picture = models.ImageField()
    review = models.FloatField()
    title = models.CharField(max_length=20)
    price = models.FloatField()
   
    def __str__(self) :
        return self.title

class Blog(models.Model):
    pp = models.ImageField()
    title = models.CharField(max_length=50)
    author = models.CharField(max_length=15)
    date = models.DateTimeField(auto_now_add=True) #set time when an instance is created
    text = models.CharField(max_length=100)

    def __str__(self) :
        return self.author

class Customer(models.Model):
    name = models.CharField(max_length=20)
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True) 

    def __str__(self):
        return self.name


class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, blank=True, null=True)
    date_ordered = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False, null=True, blank=False)
    transaction_id = models.CharField(max_length=20, null=True)

    def __str__(self):
        return str(self.id)
    
class OrderItem(models.Model): 
    product = models.ForeignKey(Arrivals, on_delete=models.SET_NULL, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True) 
    quantity = models.IntegerField(default=0, null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)

    @property
    def get_total(self):
        total = self.product.price * self.quantity
        return total

    @property
    def get_cart_total(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.get_total for item in orderitems])
        return total
    
