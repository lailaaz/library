from django.shortcuts import render

from rest_framework import generics, viewsets

from author import serializers
from author.models import Author


class AuthorViewset(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = serializers.AuthorSerializer
