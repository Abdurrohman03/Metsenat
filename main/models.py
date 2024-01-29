from django.db import models


class TolovTuri(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'To\'lov turi'
        verbose_name_plural = "To'lov turlari"


class OTM(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Oliy ta'lim Muassasasi"
        verbose_name_plural = "Oliy ta'lim Muassasalari"

