from rest_framework import serializers
from .models import Todo
from account.serializers import UserSerializer


class TodoSerializer(serializers.ModelSerializer):
    created_by = UserSerializer(read_only=True)
    class Meta:
        model = Todo
        fields = '__all__'