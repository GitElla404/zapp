from django.contrib import admin
from import_export.admin import ExportMixin
from .models import User, Product, Purchase, Seller
from .resources import ProductResource, PurchaseResource

admin.site.register(User)

admin.site.register(Seller)

@admin.register(Product)
class ProductAdmin(ExportMixin, admin.ModelAdmin):
    resource_class = ProductResource
    list_display = ('title', 'seller__shop_name', 'price', 'for_sale', 'status', 'allow_product_creation')
    search_fields = ('title', 'seller__shop_name')
    list_filter = ('status', 'for_sale', 'seller__shop_name')
    
    

@admin.register(Purchase)
class PurchaseAdmin(admin.ModelAdmin):
    resource_class = PurchaseResource
    list_display = ('buyer', 'product', 'purchase_date')
    search_fields = ('buyer__username', 'product__title')
    list_filter = ('purchase_date', 'product')

