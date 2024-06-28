from django.db import models
from django.contrib.auth.models import User

class Products(models.Model):
    product_name=models.CharField(max_length=100)
    desc = models.CharField(max_length=250)
    options =(
        ('Mobile Phone','MobilePhone'),
        ('Laptop','Laptop'),
        ('Tablet','Tablet'),
        ('Smart Watch','Smart Watch'),
    )
    category=models.CharField(max_length=100,choices=options)
    image=models.ImageField(upload_to='product_images')
    price=models.PositiveIntegerField()

    def __str__(self) -> str:
        return self.product_name

class Cart(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    products=models.ForeignKey(Products,on_delete=models.CASCADE)
    date=models.DateTimeField(auto_now_add=True)

class Order(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    products=models.ForeignKey(Products,on_delete=models.CASCADE)
    date=models.DateTimeField(auto_now_add=True)
    address=models.CharField(max_length=300)
    phone=models.IntegerField()
    options =(
        ("Order Placed","Order Placed"),
        ("Shipped","Shipped"),
        ("Out for delivery","Out for delivery"),
        ("Delivered","Delivered"),
    )
    status=models.CharField(max_length=100,default='Order placed',choices=options)