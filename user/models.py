from django.db import models
from django.utils.safestring import mark_safe
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.conf import settings
from rest_framework_simplejwt.tokens import RefreshToken
from django.db.models.signals import pre_save
from phonenumber_field.modelfields import PhoneNumberField


class Account(AbstractBaseUser):
    ROLE = (
        (0, 'Student'),
        (1, 'Homiy'),
        (2, 'Admin'),
    )
    full_name = models.CharField(max_length=50, verbose_name='Full name', null=True)
    image = models.ImageField(upload_to=image_path, null=True, blank=True)
    phone = PhoneNumberField(null=False, blank=False, unique=True)
    bio = models.TextField()
    role = models.IntegerField(choices=ROLE, default=1)
    is_superuser = models.BooleanField(default=False, verbose_name='Super user')
    is_staff = models.BooleanField(default=False, verbose_name='Staff user')
    is_active = models.BooleanField(default=True, verbose_name='Active user')
    date_modified = models.DateTimeField(auto_now=True, verbose_name='Date modified')
    date_created = models.DateTimeField(auto_now_add=True, verbose_name='Date created')

    USERNAME_FIELD = 'full_name'
    REQUIRED_FIELDS = []

    def __str__(self):
        if self.full_name:
            return f'{self.full_name}'

    def image_tag(self):
        if self.image:
            return mark_safe(f'<a href="{self.image.url}"> <img src="{self.image.url}" style="height:150px;"/> </a>' )
        return 'Image not found'

    @property
    def image_url(self):
        if self.image:
            if settings.DEBUG:
                return f'{settings.LOCAL_BASE_URL}{self.image.url}'
            return f'{settings.PROD_BASE_URL}{self.image.url}'
        return None

    @property
    def tokens(self):
        refresh = RefreshToken.for_user(self)
        data = {
            'refresh': str(refresh),
            'access': str(refresh.access_token)
        }
        return data


def account_pre_save(instance, sender, *args, **kwargs):
    if instance.role == 2:
        instance.is_staff = True
    else:
        instance.is_staff = False
    return instance


pre_save.connect(account_pre_save, sender=Account)
