from rest_framework import serializers
from phonenumber_field.serializerfields import PhoneNumberField
from user.models import Homiy, Student


class LegalEntityHomiySerializer(serializers.ModelSerializer):
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


class HomiyPOSTSerializer(serializers.ModelSerializer):
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


class HomiylarGETSerializer(serializers.ModelSerializer):
    date_joined = serializers.DateTimeField(format='%d-%m-%Y')
    holat = serializers.CharField(source='get_holat_display')

    class Meta:
        model = Homiy
        fields = ('id', 'full_name', 'phone', 'tolov_summasi', 'sarflangan_summa', 'date_joined', 'holat')

    def get_holat_display(self, obj):
        return dict(Homiy.HOLAT).get(obj.holat)


class HomiyGETSerializer(serializers.ModelSerializer):
    class Meta:
        model = Homiy
        fields = ('id', 'full_name', 'phone', 'tolov_summasi')


class HomiyUpdateSerializer(serializers.ModelSerializer):
    holat = serializers.CharField(source='get_holat_display')

    class Meta:
        model = Homiy
        fields = ('full_name', 'phone', 'holat', "tolov_summasi", 'tolov_turi')


class TalabalarListCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ('id', 'full_name', 'talabalik_turi', 'otm', 'kontrakt_miqdori', 'ajratilgan_summa')

