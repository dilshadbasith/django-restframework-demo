from rest_framework import serializers
from .models import Movie
from account.serializers import UserSerializer

class MovieSerializer(serializers.ModelSerializer):
    created_by = UserSerializer(read_only=True)
    class Meta:
        model = Movie
        fields = '__all__'