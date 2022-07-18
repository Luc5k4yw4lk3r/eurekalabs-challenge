from rest_framework import serializers
from core.models import User


# Register serializer
class RegisterSerializer(serializers.ModelSerializer):

    password = serializers.CharField(
        write_only=True,
        required=True,
        style={'input_type': 'password', 'placeholder': 'Password'}
    )
    email = serializers.EmailField(
        required=True,
        style={'input_type': 'email', 'placeholder': 'Email will be the username for login'}
    )
    name = serializers.CharField(required=True, label="Name")
    last_name = serializers.CharField(required=True, label="Last Name")

    class Meta:
        model = User
        fields = ('email', 'password', 'name', 'last_name')

    def create(self, validated_data):
        user = User.objects.create_user(email=validated_data['email'], password=validated_data['password'],
                                        name=validated_data['name'], last_name=validated_data['last_name'])
        return user


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'email', 'name', 'last_name')