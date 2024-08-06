from django.shortcuts import render
from .models import Products
from django.views.generic import ListView,DetailView,DeleteView,CreateView,UpdateView
# Create your views here.

def home(request):
    products = Products.objects.all()

    context = {'products':products}
    return render(request,'Products/home.html',context)

class ProductsList(ListView):
    model = Products
    template_name = 'Products/home.html'
    context_object_name='products'
    ordering = ['-order_date']
