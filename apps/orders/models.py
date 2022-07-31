from django.db import models

from apps.product.models import Product
from apps.authuser.models import User

class Order(models.Model):
    HOME = 'When receiving'

    PAYMENT_METHOD_CHOICES = (
        (HOME, 'When receiving'),
    )

    ORDERED     = 'ordered'
    SHIPPED     = 'shipped'
    RECEIVED    = 'received'


    STATUS_CHOICES = (
        (ORDERED,'ordered' ),
        (SHIPPED, 'shipped'),
        (RECEIVED, 'received')
    )

    customer        = models.ForeignKey(User, related_name='orders', on_delete=models.CASCADE, blank = True, null=True)
    first_name      = models.CharField(max_length=255)
    last_name       = models.CharField(max_length=255)
    email           = models.EmailField()
    phone           = models.CharField(max_length=60)
    address         = models.TextField()

    created_at      = models.DateTimeField(auto_now_add=True)
    
    paid_amount     = models.IntegerField(blank=True, null=True)
    payment_method  = models.CharField(max_length=255 ,choices = PAYMENT_METHOD_CHOICES,default=HOME) 
    paid            = models.BooleanField(default=False)

    status          = models.CharField(max_length=255,choices = STATUS_CHOICES,default=ORDERED )

    class Meta:
        ordering = ['-created_at']
    
    def __str__(self):
        return self.created_at



class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name='items', on_delete=models.CASCADE)
    price = models.IntegerField()
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return '%s' % self.id

    def get_total_price(self):
        return self.price * self.quantity
    