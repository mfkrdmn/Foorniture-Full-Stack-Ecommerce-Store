from django.shortcuts import render
from .models import *
# Create your views here.

def index(request):

    sliderParts = Slider.objects.all()
    newArrivals = Arrivals.objects.all()
    featureProducts = Featured.objects.all()
    blogPost = Blog.objects.all()
    cartItems = OrderItem.objects.all()
    order= Order.objects.get_or_create(complete=False)
    
    context = {

     "sliderParts" : sliderParts, 
     "newArrivals": newArrivals,
     "featureds" :featureProducts,
     "blogPost": blogPost,
     "cartItems" : cartItems,
     "order" : order,
    
    }


    return render(request, "index.html", context)

