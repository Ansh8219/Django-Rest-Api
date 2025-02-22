# accounts/serializers.py
from rest_framework import serializers
from .models import CustomUser

class CustomUserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = CustomUser
        fields = ('id', 'username', 'email', 'password', 'date_joined')
        read_only_fields = ('date_joined',)

    def create(self, validated_data):
        # Use the custom manager's create_user for proper password handling
        user = CustomUser.objects.create_user(
            email=validated_data.get('email'),
            username=validated_data.get('username'),
            password=validated_data.get('password')
        )
        return user
