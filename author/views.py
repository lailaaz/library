from django.shortcuts import render

from rest_framework import viewsets, permissions
from rest_framework.permissions import IsAuthenticated

from author import serializers
from author.models import Author, Category, Book, Branch, BranchBookStock, Bill, Invoice


class AuthorViewset(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = serializers.AuthorSerializer
    permission_classes = [IsAuthenticated, ]

class CategoryViewset(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = serializers.CategorySerializer
    permission_classes = [IsAuthenticated, ]

class BookViewset(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = serializers.BookSerializer
    permission_classes = [IsAuthenticated, ]

class BranchViewset(viewsets.ModelViewSet):
    queryset = Branch.objects.all()
    serializer_class = serializers.BranchSerializer
    permission_classes = [IsAuthenticated, ]

class BranchBookStockViewset(viewsets.ModelViewSet):
    queryset = BranchBookStock.objects.all()
    serializer_class = serializers.BranchBookStockSerializer
    permission_classes = [IsAuthenticated, ]

class BillViewset(viewsets.ModelViewSet):
    queryset = Bill.objects.all()
    serializer_class = serializers.BillSerializer
    permission_classes = [IsAuthenticated, ]

class InvoiceViewset(viewsets.ModelViewSet):
    queryset = Invoice.objects.all()
    serializer_class = serializers.InvoiceSerializer
    permission_classes = [IsAuthenticated, ]

