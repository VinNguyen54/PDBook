from django.urls import path

from .views import cart_detail, checkout, success, add_to_cart
urlpatterns = [
    path('', cart_detail, name='cart'),
    path('add_to_cart/<int:product_id>/', add_to_cart, name = 'add_to_cart'),
    path('checkout/', checkout, name='checkout'),
    path('success/', success, name='success'),
]