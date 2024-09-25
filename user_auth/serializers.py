from rest_framework import serializers
from django.contrib.auth import authenticate
from user_auth.models import CustomUser

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    mobile_number = serializers.CharField(required=False, allow_blank=True)

    class Meta:
        model = CustomUser
        fields = ['username', 'password', 'email','mobile_number']

    def create(self, validated_data):
        
        mobile_number = validated_data.pop('mobile_number', None)
        
        user = CustomUser.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password'],
        )
        
        if mobile_number:
            user.mobile_number = mobile_number
            user.save()
            
        return user

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)
    email = serializers.EmailField(required=False)
    mobile_number = serializers.CharField(required=False)

    def validate(self, data):
        user = authenticate(**data)
        if user and user.is_active:
             return user
        raise serializers.ValidationError("Invalid Credentials")