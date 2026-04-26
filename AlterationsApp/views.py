from django.shortcuts import render, get_object_or_404, redirect
from .models import Order
from django.conf import settings

# Create your views here.

# need order_list
# need order_detail
def home(request):
    return render(request, 'AlterationsApp/home.html', {})


# need to filter orders by user
def order_list(request):
    orders = Order.objects.filter(customer_name=request.user).order_by('id')
    return render(request, 'AlterationsApp/order_list.html', {'orders' : orders})

def order_detail(request, pk):
    order = get_object_or_404(Order, pk=pk)
    return render(request, 'AlterationsApp/order_detail.html', {'order' : order})