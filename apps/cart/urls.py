from django.urls import path

from .views import cart_detail, checkout, success

urlpatterns = [
    path('', cart_detail, name='cart'),
    path('checkout/', checkout, name='checkout'),
    path('success/', success, name='success'),
]