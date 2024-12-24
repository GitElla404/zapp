from django.urls import path, include 
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, SellerViewSet, PurchaseViewSet, OrderHistoryViewSet, SalesHistoryViewSet


router = DefaultRouter()
router.register(r'createuser', UserViewSet, basename='user')
router.register(r'createseller', SellerViewSet, basename='seller')
router.register(r'orders', PurchaseViewSet, basename='purchase')

urlpatterns = [
    path('order-history/', OrderHistoryViewSet.as_view({'get': 'list'}), name='order-history'),
    path('sales-history/', SalesHistoryViewSet.as_view({'get': 'list'}), name='sales-history'),
    path('', include(router.urls)),
]