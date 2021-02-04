import random

from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status

from .models import Product, User
from .serializers import ProductSerializer

class ProductViewSet(ViewSet):

    def list(self, request):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = ProductSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status.HTTP_201_CREATED)

    def retrieve(self, request, pk=None):
        product = Product.objects.get(id=pk)
        serializer = ProductSerializer(product)
        return Response(serializer.data, status.HTTP_200_OK)


    def update(self, request, pk=None):
        product = Product.objects.get(id=pk)
        serializer = ProductSerializer(instance=product, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(request.data, status.HTTP_202_ACCEPTED)

    def destroy(self, request, pk=None):
        try:
            product = Product.objects.get(id=pk)
            product.delete()
            return Response({"message": "Product deleted"}, status=status.HTTP_204_NO_CONTENT)
        except:
            return Response({"message": "Product not found"}, status=status.HTTP_400_BAD_REQUEST)


class UserAPIView(APIView):

    def get(self, request):
        users = User.objects.all()
        user = random.choice(users)
        return Response(
            {"id": user.id}
        )





