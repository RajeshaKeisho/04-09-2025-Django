from django.contrib import admin
from .models import Customer, Address, Product, Category, Order
# Register your models here.

admin.site.register(Customer)
admin.site.register(Address)
admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Order)