from django.shortcuts import render

from rest_framework import generics

from author import serializers
from author.models import Author
from author.serializers import AuthorSerializer


class AuthorViewset(generics.APIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
