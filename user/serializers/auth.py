from rest_framework import serializers


class RegisterSerializer(serializers.Serializer):
    first_name = serializers.CharField(required=True, min_length=2)
    last_name = serializers.CharField(required=True, min_length=2)
    email = serializers.EmailField(required=True, min_length=2)
    password = serializers.CharField(required=True, min_length=8)

class LoginSerializer(serializers.Serializer):
    username = serializers.EmailField(required=True, min_length=2)
    password = serializers.CharField(required=True, min_length=8)