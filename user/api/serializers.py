from django.contrib.auth import authenticate
from django.contrib.auth.models import update_last_login
from rest_framework import serializers
from rest_framework_jwt.settings import api_settings
from user.models import User
from rest_framework import serializers
from phonenumber_field.serializerfields import PhoneNumberField
from user.models import Homiy


class LegalEntityHomiySerializer(serializers.Serializer):
    full_name = serializers.CharField(max_length=255)
    phone = PhoneNumberField()
    tolov_summasi = serializers.IntegerField()
    tashkilot_nomi = serializers.CharField(max_length=50)

    class Meta:
        model = Homiy
        fields = ('id', 'full_name', 'phone', 'tolov_summasi', 'tashkilot_nomi')

    def create(self, validated_data):
        homiy = Homiy.objects.create(**validated_data)
        homiy.role = 1
        homiy.save()
        return homiy

    def update(self, instance, validated_data):
        instance.full_name = validated_data.get('full_name', instance.full_name)
        instance.role = 1
        instance.phone_number = validated_data.get('phone_number', instance.phone_number)
        instance.tolov_summasi = validated_data.get('tolov_summasi', instance.tolov_summasi)
        instance.tashkilot_nomi = validated_data.get('tashkilot_nomi', instance.tashkilot_nomi)
        instance.save()
        return instance


class HomiySerializer(serializers.Serializer):
    full_name = serializers.CharField(max_length=255)
    phone = PhoneNumberField()
    tolov_summasi = serializers.IntegerField()

    class Meta:
        model = Homiy
        fields = ('id', 'full_name', 'phone', 'tolov_summasi')

    def create(self, validated_data):
        homiy = Homiy.objects.create(**validated_data)
        homiy.save()
        return homiy

    def update(self, instance, validated_data):
        instance.full_name = validated_data.get('full_name', instance.full_name)
        instance.role = 1
        instance.phone_number = validated_data.get('phone_number', instance.phone_number)
        instance.tolov_summasi = validated_data.get('tolov_summasi', instance.tolov_summasi)
        instance.save()
        return instance


JWT_PAYLOAD_HANDLER = api_settings.JWT_PAYLOAD_HANDLER
JWT_ENCODE_HANDLER = api_settings.JWT_ENCODE_HANDLER


class UserLoginSerializer(serializers.Serializer):
    email = serializers.CharField(max_length=255)
    password = serializers.CharField(max_length=128, write_only=True)
    token = serializers.CharField(max_length=255, read_only=True)

    def validate(self, data):
        email = data.get("email", None)
        password = data.get("password", None)
        user = authenticate(email=email, password=password)
        if user is None:
            raise serializers.ValidationError(
                'A user with this email and password is not found.'
            )
        try:
            payload = JWT_PAYLOAD_HANDLER(user)
            jwt_token = JWT_ENCODE_HANDLER(payload)
            update_last_login(None, user)
        except User is None:
            raise serializers.ValidationError(
                'User with given email and password does not exists'
            )
        return {
            'email': user.email,
            'token': jwt_token
        }
