from rest_framework import serializers
from .models import PerfilViajante, Trip, Resumo, ResumoDate
from django.utils.formats import number_format


class PerfilViajanteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = PerfilViajante
        fields = ["id", 'name']


class TripSerializer(serializers.ModelSerializer):
    # tipo_viajante = serializers.ReadOnlyField(source='tipo_viajante.name')
    hospedagem = serializers.SerializerMethodField('hospedagem1')
    alimentacao = serializers.SerializerMethodField('alimentacao1')
    extra = serializers.SerializerMethodField('extra1')
    passagem = serializers.SerializerMethodField('passagem1')
    wallet = serializers.SerializerMethodField('wallet1')
    total = serializers.SerializerMethodField('total1')
    remaining_days = serializers.ReadOnlyField()
    percent = serializers.ReadOnlyField()
    income = serializers.ReadOnlyField()
    milhas = serializers.ReadOnlyField()

    class Meta:
        model = Trip
        fields = [
            "id",
            'tipo_viajante',
            'hospedagem',
            'alimentacao',
            'extra',
            'passagem',
            "total",
            "destination",
            "income",
            "trip_date",
            "remaining_days",
            "wallet",
            "percent",
            "milhas",
        ]

    def hospedagem1(self, obj):
        return number_format(obj.hospedagem)

    def alimentacao1(self, obj):
        return number_format(obj.alimentacao)

    def extra1(self, obj):
        return number_format(obj.extra)

    def passagem1(self, obj):
        return number_format(obj.passagem)

    def total1(self, obj):
        return number_format(obj.total)

    def wallet1(self, obj):
        return number_format(obj.wallet)


class ResumoSerializer(serializers.ModelSerializer):

    num_months = serializers.ReadOnlyField()
    money_end = serializers.SerializerMethodField('money_end1')
    money_month = serializers.SerializerMethodField('money_month1')
    date = serializers.ReadOnlyField()
    trip_cost = serializers.SerializerMethodField('trip_cost1')
    income = serializers.SerializerMethodField('income1')

    class Meta:
        model = Resumo
        fields = [
            "id",
            'trip',
            'date',
            'trip_date',
            'num_months',
            'money_end',
            'money_month',
            "trip_cost",
            "income",
        ]

    def money_end1(self, obj):
        return number_format(obj.money_end)

    def money_month1(self, obj):
        return number_format(obj.money_month)

    def trip_cost1(self, obj):
        return number_format(obj.trip_cost)

    def income1(self, obj):
        return number_format(obj.income)


class ResumoDateSerializer(serializers.ModelSerializer):

    num_months = serializers.ReadOnlyField()
    money_end = serializers.SerializerMethodField('money_end1')
    # money_month = serializers.SerializerMethodField('money_month1')
    trip_cost = serializers.SerializerMethodField('trip_cost1')
    income = serializers.SerializerMethodField('trip_cost1')
    date = serializers.ReadOnlyField()

    class Meta:
        model = ResumoDate
        fields = [
            "id", 'trip', 'trip_date', 'date', 'num_months', 'money_end',
            'money_month', "trip_cost", "income"
        ]

    def money_end1(self, obj):
        return number_format(obj.money_end)

    def money_month1(self, obj):
        return number_format(obj.money_month)

    def trip_cost1(self, obj):
        return number_format(obj.trip_cost)

    def income1(self, obj):
        return number_format(obj.income)