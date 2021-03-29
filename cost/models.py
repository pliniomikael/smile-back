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
    destination = models.CharField(max_length=50, null=True)
    income = models.DecimalField(max_digits=9, decimal_places=2, null=True)
    trip_date = models.DateField(auto_now=False, auto_now_add=False, null=True)
    hospedagem = models.DecimalField(max_digits=9, decimal_places=2)
    alimentacao = models.DecimalField(max_digits=9, decimal_places=2)
    extra = models.DecimalField(max_digits=9, decimal_places=2)
    passagem = models.DecimalField(max_digits=9, decimal_places=2)
    total = models.DecimalField(max_digits=9, decimal_places=2, null=True)
    remaining_days = models.IntegerField(null=True)
    percent = models.FloatField(null=True)
    milhas = models.FloatField(null=True)
    wallet = models.DecimalField(max_digits=9, decimal_places=2, null=True)

    def save(self, *args, **kwargs):
        self.income = "%.2f" % (float(self.wallet) * float(0.03975))
        d_days = self.trip_date - datetime.date.today()
        self.remaining_days = d_days.days
        self.total = self.hospedagem + self.alimentacao + self.extra + self.passagem
        self.percent = "%.2f" % ((self.wallet * 100) / self.total)
        self.milhas = self.wallet * 6

        super(Trip, self).save(*args, **kwargs)

    class Meta:
        verbose_name = "Trip"
        verbose_name_plural = "Trip"

    def __str__(self):
        return self.tipo_viajante.name


class Resumo(models.Model):

    trip = models.ForeignKey(Trip, on_delete=models.CASCADE)
    date = models.DateField(auto_now=False, auto_now_add=False)
    income = models.DecimalField(max_digits=9, decimal_places=2, null=True)

    trip_date = models.DateField(auto_now=False, auto_now_add=False)
    money_end = models.DecimalField(max_digits=9, decimal_places=2, null=True)
    money_month = models.DecimalField(max_digits=9,
                                      decimal_places=2,
                                      null=True)
    num_months = models.IntegerField()
    trip_cost = models.DecimalField(max_digits=9, decimal_places=2, null=True)

    def save(self, *args, **kwargs):
        self.date = datetime.date.today()

        self.num_months = (self.trip_date.year - self.date.year) * 12 + (
            self.trip_date.month - self.date.month)
        self.money_end = float(self.trip.total) + float(
            float(self.trip.total) * float(0.03975))
        self.money_month = self.trip.total / self.num_months
        self.trip_cost = self.trip.total
        self.income = "%.2f" % (float(self.trip_cost) * float(0.03975))
        super(Resumo, self).save(*args, **kwargs)

    class Meta:
        verbose_name = "Resumo"
        verbose_name_plural = "Resumos"

    def __str__(self):
        return self.trip.tipo_viajante.name


class ResumoDate(models.Model):

    trip = models.ForeignKey(Trip, on_delete=models.CASCADE)
    money_month = models.DecimalField(max_digits=9, decimal_places=2)
    money_end = models.DecimalField(max_digits=9, decimal_places=2, null=True)
    date = models.DateField(auto_now=False, auto_now_add=False)
    trip_date = models.DateField(auto_now=False, auto_now_add=False)
    num_months = models.IntegerField()
    trip_cost = models.DecimalField(max_digits=9, decimal_places=2, null=True)
    income = models.DecimalField(max_digits=9, decimal_places=2, null=True)

    def save(self, *args, **kwargs):
        self.num_months = math.ceil(self.trip.total / self.money_month)
        self.date = datetime.datetime.now()
        self.trip_date = self.date + relativedelta(months=self.num_months)
        self.money_end = float(self.trip.total) + float(
            float(self.trip.total) * float(0.03975))
        self.trip_cost = self.trip.total
        self.income = "%.2f" % (float(self.trip_cost) * float(0.03975))
        super(ResumoDate, self).save(*args, **kwargs)

    class Meta:
        verbose_name = "ResumoDate"
        verbose_name_plural = "ResumoDates"

    def __str__(self):
        return self.trip.tipo_viajante.name
