from django.urls import path
from . import views

# add urlpatterns list https://tutorial.djangogirls.org/en/django_urls/

# need index page
# need order list (which will list all of the user's orders)
# need order detail (user clicks on one order in the list of orders to get a detailed page, like in the blog example)
urlpatterns = [
    path('', views.home, name='home'),
    path('order_list', views.order_list, name='order_list'),
    path('order/<int:pk>/', views.order_detail, name='order_detail'),
]