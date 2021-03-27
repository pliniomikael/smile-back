from django.db import models
from django.template.defaultfilters import slugify
from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
import math
import datetime
from dateutil.relativedelta import relativedelta


class PerfilViajante(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        verbose_name = "perfilviajante"
        verbose_name_plural = "perfilviajantes"

    def __str__(self):
        return self.name


class Trip(models.Model):

    tipo_viajante = models.ForeignKey(PerfilViajante, on_delete=models.CASCADE)
    hospedagem = models.DecimalField(max_digits=9, decimal_places=2)
    alimentacao = models.DecimalField(max_digits=9, decimal_places=2)
    extra = models.DecimalField(max_digits=9, decimal_places=2)
    passagem = models.DecimalField(max_digits=9, decimal_places=2)
    total = models.DecimalField(max_digits=9, decimal_places=2, null=True)

    def save(self, *args, **kwargs):
        self.total = self.hospedagem + self.alimentacao + self.extra + self.passagem
        super(Trip, self).save(*args, **kwargs)

    class Meta:
        verbose_name = "Trip"
        verbose_name_plural = "Trip"

    def __str__(self):
        return self.tipo_viajante.name


class Resumo(models.Model):

    trip = models.ForeignKey(Trip, on_delete=models.CASCADE)
    date_initial = models.DateField(auto_now=False, auto_now_add=False)
    date_end = models.DateField(auto_now=False, auto_now_add=False)
    money_end = models.DecimalField(max_digits=9, decimal_places=2, null=True)
    money_month = models.DecimalField(max_digits=9,
                                      decimal_places=2,
                                      null=True)
    num_months = models.IntegerField()

    def save(self, *args, **kwargs):
        print(self.trip.total)
        self.num_months = (self.date_end.year -
                           self.date_initial.year) * 12 + (
                               self.date_end.month - self.date_initial.month)
        self.money_end = float(self.trip.total) + float(
            float(self.trip.total) * float(0.03975))
        self.money_month = self.trip.total / self.num_months
        super(Resumo, self).save(*args, **kwargs)

    class Meta:
        verbose_name = "Resumo"
        verbose_name_plural = "Resumos"

    def __str__(self):
        return self.trip.tipo_viajante.name


class ResumoDate(models.Model):

    trip = models.ForeignKey(Trip, on_delete=models.CASCADE)
    money_month = models.DecimalField(max_digits=9,
                                      decimal_places=2,
                                      null=True)
    date_initial = models.DateField(auto_now=False, auto_now_add=False)
    date_end = models.DateField(auto_now=False, auto_now_add=False)
    money_end = models.DecimalField(max_digits=9, decimal_places=2, null=True)
    num_months = models.IntegerField()

    def save(self, *args, **kwargs):
        print(self.trip.total)
        self.num_months = math.ceil(self.trip.total / self.money_month)
        self.date_initial = datetime.datetime.now()
        self.date_end = self.date_initial + relativedelta(
            months=self.num_months)
        self.money_end = float(self.trip.total) + float(
            float(self.trip.total) * float(0.03975))
        super(ResumoDate, self).save(*args, **kwargs)

    class Meta:
        verbose_name = "ResumoDate"
        verbose_name_plural = "ResumoDates"

    def __str__(self):
        return self.trip.tipo_viajante.name
