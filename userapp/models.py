from django.db import models
from django.contrib.auth.models import User

class User (models.Model):
    CARD_TYPE = (
        ('pending', 'Pending'),
        ('visa', 'Visa'),
        ('mastercard', 'MasterCard'),
        ('wema', 'Wema'),
    )
    
    fullname = models.TextField()
    email = models.EmailField(unique=True)
    pswd = models.TextField()
    shipping_address = models.TextField()
    phone_number = models.IntegerField() 
    card_number = models.IntegerField()
    card_type = models.CharField(max_length=20, choices=CARD_TYPE, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)
    
    def save(self, *args, **kwargs):
            self.fullname = self.fullname.capitalize()
            super().save(*args, **kwargs)
    
    def __str__(self):
        return self.fullname


class Seller (models.Model):
    CARD_TYPE = (
        ('pending', 'Pending'),
        ('visa', 'Visa'),
        ('mastercard', 'MasterCard'),
        ('wema', 'Wema'),
    )
    
    fullname = models.TextField()
    email = models.EmailField(unique=True)
    pswd = models.TextField()
    shop_name = models.TextField()
    home_address = models.TextField()
    shop_address = models.TextField()
    phone_number = models.IntegerField() 
    card_number = models.IntegerField()
    tin_number = models.IntegerField()
    card_type = models.CharField(max_length=20, choices=CARD_TYPE, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)
    
    def save(self, *args, **kwargs):
            self.fullname = self.fullname.capitalize()
            super().save(*args, **kwargs)
    
    def __str__(self):
        return self.fullname


class Product(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=50, choices=[('pending', 'Pending'), ('completed', 'Completed')])
    seller = models.ForeignKey(Seller, related_name='product', on_delete=models.CASCADE)
    for_sale = models.BooleanField(default=False)  
    
    allow_product_creation = models.BooleanField(default=True)

    def __str__(self):
        return f"Allow Product Creation: {self.allow_product_creation}"

class Purchase(models.Model):
    buyer = models.ForeignKey(User, related_name='purchases', on_delete=models.CASCADE)
    seller = models.ForeignKey(Seller, related_name='sales', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name='purchases', on_delete=models.CASCADE)
    purchase_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.buyer.fullname} bought {self.product.title} on {self.purchase_date}'
    
