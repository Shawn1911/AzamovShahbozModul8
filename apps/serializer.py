from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from rest_framework.exceptions import ValidationError
from rest_framework.fields import CharField, EmailField, UUIDField
from rest_framework.serializers import ModelSerializer

from apps.models import Category, Product


class UserRegisterModelSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = 'username', 'email', 'password', 'confirm_password'
        extra_kwargs = {
            'password': {'write_only': True}
        }

    confirm_password = CharField(write_only=True)
    email = EmailField()

    def validate(self, data):
        if data.get('password') != data.get('confirm_password'):
            raise ValidationError("Passwords do not match.")
        return data

    def create(self, validated_data):
        validated_data.pop('confirm_password', None)  # Remove confirm_password from validated_data
        validated_data['password'] = make_password(validated_data['password'])
        return super().create(validated_data)


class CategoryListSerializer(ModelSerializer):
    id = UUIDField(read_only=True)

    class Meta:
        model = Category
        exclude = ()


class ProductListSerializer(ModelSerializer):
    id = UUIDField(read_only=True)

    class Meta:
        model = Product
        exclude = ()


class UserSerializer(ModelSerializer):
    id = UUIDField(read_only=True)

    class Meta:
        model = User
        fields = '__all__'
