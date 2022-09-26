from pyexpat import model
from django.db import models

from apps.product.models import Product
from apps.authuser.models import User

class Order(models.Model):

    # payment method 
    CASH =  'cash'

    PAYMENT_METHOD_CHOICES = (
        (CASH, 'cash'),
    )


    # status 
    P = 'Processing'
    A = 'Authorized'   
    AS = 'Awaiting Shipment' 
    D = 'Delivering'
    COM = 'Complete'
    CAN = 'Cancelled'

    STATUS_CHOICES = (
        (P, 'Processing'),
        (A, 'Authorized'),
        (AS, 'Awaiting Shipment'),
        (D, 'Delivering'),
        (COM, 'Complete'),
        (CAN, 'Cancelled')
    )


    customer        = models.ForeignKey(User, related_name='orders', on_delete=models.CASCADE, blank = True, null=True)
    first_name      = models.CharField(max_length=255)
    last_name       = models.CharField(max_length=255)
    email           = models.EmailField()
    phone           = models.CharField(max_length=60)
    address         = models.TextField()
    note            = models.TextField(blank=True, null=True)

    created_at      = models.DateTimeField(auto_now_add=True)
    
    paid            = models.BooleanField(default=False)
    paid_amount     = models.DecimalField(max_digits=6, decimal_places=2, blank= True, null= True)
    payment_method  = models.CharField(max_length=255 ,choices = PAYMENT_METHOD_CHOICES,default=CASH) 
    status          = models.CharField(max_length=255, choices=STATUS_CHOICES, default=P)

    class Meta:
        ordering = ['-created_at']
    
    def __str__(self):
        return self.last_name



class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name='items', on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=6, decimal_places=2) 
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return '%s' % self.id
    