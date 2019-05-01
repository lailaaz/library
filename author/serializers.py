from rest_framework import serializers

from author import models


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
           '__all__'
        )
        model = models.Author


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            '__all__'
        )
        model = models.Category


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            '__all__'
        )
        model = models.Book


class BranchSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            '__all__'
        )
        model = models.Branch


class BranchBookStockSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            '__all__'
        )
        model = models.BranchBookStock


class BillSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            '__all__'
        )
        model = models.Bill


class InvoiceSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            '__all__'
        )
        model = models.Invoice


