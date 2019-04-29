from rest_framework import serializers

from author import models


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
           '__all__'
        )
        model = models.Author