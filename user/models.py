from django.db import models
from django.utils.safestring import mark_safe
from django.contrib.auth.models import AbstractUser, User
from django.conf import settings
from rest_framework_simplejwt.tokens import RefreshToken
from phonenumber_field.modelfields import PhoneNumberField
from main.models import TolovTuri, OTM


def image_path(instance, filename):
    return f'accounts/{instance.id}/{filename}'


class Homiy(AbstractUser):
    HOLAT = (
        (0, 'Yangi'),
        (1, 'Moderatsiyada'),
        (2, 'Tasdiqlangan'),
        (3, 'Bekor qilingan')
    )
    ROLE = (
        (0, 'Jismoniy shaxs'),
        (1, 'Yuridik shaxs'),
    )
    first_name = None
    last_name = None
    full_name = models.CharField(max_length=50, verbose_name='Full name', null=True)
    image = models.ImageField(upload_to=image_path, null=True, blank=True)
    phone = PhoneNumberField(null=False, blank=False, unique=True, verbose_name='Telefon raqam')
    role = models.IntegerField(choices=ROLE, default=0, verbose_name='Shaxs')
    date_joined = models.DateTimeField(auto_now_add=True, verbose_name='Date created')
    tolov_summasi = models.IntegerField(null=True, blank=True)
    holat = models.IntegerField(choices=HOLAT, default=0)
    tashkilot_nomi = models.CharField(max_length=255, null=True, blank=True)
    sarflangan_summa = models.IntegerField(null=True, blank=True)
    tolov_turi = models.ForeignKey(TolovTuri, on_delete=models.CASCADE, null=True, blank=True)
    groups = None
    user_permissions = None
    is_superuser = False
    username = None
    is_staff = False
    is_active = False
    password = None

    USERNAME_FIELD = 'full_name'

    def __str__(self):
        return f'{self.full_name}'

    @property
    def tokens(self):
        refresh = RefreshToken.for_user(self)
        data = {
            'refresh': str(refresh),
            'access': str(refresh.access_token)
        }
        return data

    class Meta:
        verbose_name = 'Homiy'
        verbose_name_plural = 'Homiylar'


class Student(User):
    TALABALIK_TURI = (
        (0, 'Bakalavr'),
        (1, 'Magistratura')
    )
    full_name = models.CharField(max_length=50)
    talabalik_turi = models.IntegerField(choices=TALABALIK_TURI, default=0)
    otm = models.ForeignKey(OTM, on_delete=models.SET_NULL, null=True)
    kontrakt_miqdori = models.IntegerField()
    ajratilgan_summa = models.IntegerField(null=True, blank=True)
    homiy = models.ManyToManyField(Homiy)

    def __str__(self):
        return f'{self.full_name}'

    @property
    def tokens(self):
        refresh = RefreshToken.for_user(self)
        data = {
            'refresh': str(refresh),
            'access': str(refresh.access_token)
        }
        return data

    class Meta:
        verbose_name = 'Talaba'
        verbose_name_plural = 'Talabalar'
