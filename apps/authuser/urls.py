from django.urls import path
from django.contrib.auth import views
from .views import register, userlogin ,vendor_admin, add_product, edit_product, customer_admin, remove_product
urlpatterns = [
    path('register/', register, name='register'),
    path('login/', userlogin, name = 'login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),


    path('vendor-admin/', vendor_admin, name= 'vendor_admin'),
    path('add-product/',add_product, name='add_product'),
    path('edit-product/<int:pk>/',edit_product, name='edit_product'),
    path('remove-product/<int:pk>',remove_product, name = 'remove_product'),


    path('customer-admin/',customer_admin, name='customer_admin'),
]