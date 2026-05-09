from django.shortcuts import render, get_object_or_404, redirect
from .models import Order, REQUIREMENTS
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.contrib.auth import logout
from .forms import RegistrationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .forms import OrderForm

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
    form_class = RegistrationForm
    success_url = reverse_lazy('login')
    template_name ='registration/signup.html'

@login_required
def order_request(request):
    error_message = None
    if request.method == "POST":
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)

            item = order.item
            alteration = order.alteration_type
            
            ##this is will make some measurements requried, changing based on your choices, ex. you need to hem your pants, i don't need chest measurement tho
            key = (item, alteration)
            required_fields = REQUIREMENTS.get(key, [])


            for field in required_fields:
                if not getattr(order,field, None):
                    error_message = f"{field.replace('_', ' ').title()} is required"
                    break
            if not error_message:
                order.customer_name = request.user
                order.status = 'pending'
                order.save()
                return redirect('order_list')
    else:
        form = OrderForm()
    return render(request, 'AlterationsApp/order_request.html', {'form' : form, 'error_message': error_message})

@login_required
def order_manage(request):
    unassigned_orders = Order.objects.filter(assigned_staff__isnull=True).order_by('id')
    assigned_orders = Order.objects.filter(assigned_staff=request.user).exclude(status='complete').order_by('id')
    completed_orders = Order.objects.filter(assigned_staff=request.user, status='complete').order_by('id')
    return render(request, 'AlterationsApp/order_manage.html', {'unassigned_orders' : unassigned_orders, 'assigned_orders' : assigned_orders, 'completed_orders' : completed_orders})

@login_required
def accept_order(request, pk):
    order = get_object_or_404(Order, pk=pk)
    if request.method == 'POST':
        order.assign_staff(request.user)
    return redirect('order_manage')

@login_required
def update_order_status(request, pk):
    order = get_object_or_404(Order, pk=pk)
    if request.method == "POST":
        order.status = request.POST.get('status')
        order.save()
    return redirect('order_manage')

@login_required
def cancel_order(request, pk):
    order = get_object_or_404(Order, pk=pk)
    if request.method == "POST":
        order.status = 'cancelled'
        order.save()
    return redirect('order_list')