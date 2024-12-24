from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, IsAdminUser, IsAuthenticatedOrReadOnly
from .models import User, Product, Purchase, Seller
from .serializers import UserSerializer, PurchaseSerializer, ProductSerializer, SellerSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication
from django.conf import settings
from rest_framework.response import Response
from django.db import transaction
from rest_framework import status

class SellerViewSet(viewsets.ModelViewSet):
    queryset = Seller.objects.all()
    serializer_class = SellerSerializer
    authentication_classes = [JWTAuthentication]
    
    def create_user(self, serializer):
        serializer.save(seller=self.request.seller)
        
    def get_permissions(self):
        if self.action == 'create':
            return [IsAdminUser() if not self.is_product_creation_allowed() else IsAuthenticated()]
        return super().get_permissions()
    
    def is_product_creation_allowed(self):
        system_settings = Product.objects.first()
        return system_settings and system_settings.allow_product_creation
    
    def perform_create(self, serializer):
        system_settings = Product.objects.first()
        if system_settings and not system_settings.allow_product_creation:
            raise Response(
                {"detail": "Product creation is currently disabled."},
                status=status.HTTP_403_FORBIDDEN
            )
        serializer.save(seller=self.request.seller)



class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    authentication_classes = [JWTAuthentication]
    
    def create_user(self, serializer):
        serializer.save(user=self.request.user)
        


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_permissions(self):
        if self.action == 'create':
            return [IsAuthenticated()]
        return super().get_permissions()

    def update(self, request, *args, **kwargs):
        task = self.get_object()
        if task.user != request.user and not request.user.is_staff:
            return Response({"detail": "You cannot modify someone else's task."}, status=status.HTTP_403_FORBIDDEN)
        return super().update(request, *args, **kwargs)


class PurchaseViewSet(viewsets.ModelViewSet):
    queryset = Purchase.objects.all()
    serializer_class = PurchaseSerializer
    permission_classes = [IsAuthenticated]

    @transaction.atomic
    def create(self, request, *args, **kwargs):
        product_id = request.data.get('task')
        product = Product.objects.get(id=product_id)

        if not product.for_sale:
            return Response({"detail": "This task is not for sale."}, status=status.HTTP_400_BAD_REQUEST)

        if product.user == request.user:
            return Response({"detail": "You cannot buy your own task."}, status=status.HTTP_400_BAD_REQUEST)

        purchase = Purchase.objects.create(buyer=request.user, product=product)

        product.for_sale = False
        product.save()

        return Response(PurchaseSerializer(purchase).data, status=status.HTTP_201_CREATED)
    
    

class OrderHistoryViewSet(viewsets.ViewSet):
    permission_classes = [IsAuthenticated]

    def list(self, request):
        purchases = Purchase.objects.filter(buyer=request.user).order_by('-purchase_date')
        serializer = PurchaseSerializer(purchases, many=True)
        return Response(serializer.data)


class SalesHistoryViewSet(viewsets.ViewSet):
    permission_classes = [IsAuthenticated]

    def list(self, request):
        sales = Purchase.objects.filter(seller=request.user).order_by('-purchase_date')
        serializer = PurchaseSerializer(sales, many=True)
        return Response(serializer.data)
