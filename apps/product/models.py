from django.contrib.auth.models import User
from io import BytesIO
from PIL import Image

from django.core.files import File
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

from apps.authuser.models import User

# Create your models here.
class Category(models.Model):
    title   = models.CharField(max_length=60)
    slug    = models.SlugField()

    class Meta:
        ordering = ['title']
    
    def __str__(self):
        return self.title

class Product(models.Model):
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    vendor = models.ForeignKey(User, related_name='products', on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    discount = models.IntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(100)])
    author = models.CharField(max_length=255)
    page = models.IntegerField()
    publisher = models.CharField(max_length=255)
    publish_date = models.DateField()
    total_quantity = models.IntegerField()
    date_added = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='uploads/', blank=True, null=True)
    thumbnail = models.ImageField(upload_to='uploads/', blank=True, null=True)

    class Meta:
        ordering = ['-date_added']
    
    def __str__(self):
        return self.title

    def get_discount_price(self):
       self.price = self.price - ((self.price * self.discount)/100)

    def get_thumbnail(self):
        if self.thumbnail:
            return self.thumbnail.url
        else:
            if self.image:
                self.thumbnail = self.make_thumbnail(self.image)
                self.save()

                return self.thumbnail.url
            else:
                return 'https://via.placeholder.com/240x180.jpg'
    
    def make_thumbnail(self, image, size=(300,300)):
        img = Image.open(image)
        img.convert('RGB')
        img.thumbnail(size)

        thumb_io = BytesIO()
        img.save(thumb_io, 'JPEG', quality=85)

        thumbnail = File(thumb_io, name=image.name)

        return thumbnail

    def get_rating(self):
        reviews_total = 0

        for review in self.reviews.all():
            reviews_total += review.rating

        if reviews_total > 0:
            return reviews_total /self.reviews.count()
        
        return 0

class Review(models.Model):
    product = models.ForeignKey(Product, related_name = 'reviews', on_delete=models.CASCADE)
    rating = models.IntegerField(default = 3)
    content = models.TextField()
    created_by = models.ForeignKey(User, related_name = 'reviews', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add = True)