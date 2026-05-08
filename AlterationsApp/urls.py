from django.urls import path
from . import views
from .views import SignUpView

# add urlpatterns list https://tutorial.djangogirls.org/en/django_urls/

# need index page
# need order list (which will list all of the user's orders)
# need order detail (user clicks on one order in the list of orders to get a detailed page, like in the blog example)
urlpatterns = [
    path('', views.home, name='home'),
    path('order_list', views.order_list, name='order_list'),
    path('order/<int:pk>/', views.order_detail, name='order_detail'),
    path('logout/', views.logout_view, name='logout'),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('order_request', views.order_request, name='order_request'),
    path('order_manage', views.order_manage, name='order_manage'),
    path('order/<int:pk>/accept_order/', views.accept_order, name='accept_order'),
    path('order/<int:pk>/update_status', views.update_order_status, name='update_order_status'),
]