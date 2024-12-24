from import_export import resources
from .models import Product, Purchase


class ProductResource(resources.ModelResource):
    class Meta:
        model = Product
        fields = ('id', 'title', 'description', 'price', 'status', 'seller__shop_name', 'for_sale')
    
class PurchaseResource(resources.ModelResource):
    class Meta:
        model = Purchase
        fields = ('id', 'buyer__fullname', 'seller__shop_name', 'product__title', 'purchase_date')
        
    def dehydrate_purchase_date(self, purchase):
        return purchase.purchase_date.strftime('%Y-%m-%d')
