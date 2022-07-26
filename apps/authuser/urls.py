from django.urls import path
from django.contrib.auth import views
from .views import register, userlogin ,vendor_admin

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', userlogin, name = 'login'),
     path('logout/', views.LogoutView.as_view(), name='logout'),

    path('vendor-admin/', vendor_admin, name= 'vendor_admin'),
]