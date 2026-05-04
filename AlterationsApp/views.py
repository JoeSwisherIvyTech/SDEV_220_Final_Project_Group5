from django.shortcuts import render, get_object_or_404, redirect
from .models import Order
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.contrib.auth import logout
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView

# Create your views here.

# need order_list
# need order_detail
def home(request):
    return render(request, 'AlterationsApp/home.html', {})


# need to filter orders by user
@login_required
def order_list(request):
    orders = Order.objects.filter(customer_name=request.user).order_by('id')
    return render(request, 'AlterationsApp/order_list.html', {'orders' : orders})

@login_required
def order_detail(request, pk):
    order = get_object_or_404(Order, pk=pk)
    return render(request, 'AlterationsApp/order_detail.html', {'order' : order})

def logout_view(request):
    logout(request)
    return redirect('home')

class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name ='registration/signup.html'