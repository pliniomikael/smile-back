from rest_framework import serializers
from .models import PerfilViajante, Trip, Resumo, ResumoDate


class PerfilViajanteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = PerfilViajante
        fields = ["id", 'name']


class TripSerializer(serializers.HyperlinkedModelSerializer):
    tipo_viajante = serializers.ReadOnlyField(source='tipo_viajante.name')

    total = serializers.ReadOnlyField()

    class Meta:
        model = Trip
        fields = [
            "id", 'tipo_viajante', 'hospedagem', 'alimentacao', 'extra',
            'passagem', "total"
        ]


class ResumoSerializer(serializers.HyperlinkedModelSerializer):

    num_months = serializers.ReadOnlyField()
    money_end = serializers.ReadOnlyField()
    money_month = serializers.ReadOnlyField()

    class Meta:
        model = Resumo
        fields = [
            "id",
            'trip',
            'date_initial',
            'date_end',
            'num_months',
            'money_end',
            'money_month',
        ]


class ResumoDateSerializer(serializers.HyperlinkedModelSerializer):

    num_months = serializers.ReadOnlyField()
    money_end = serializers.ReadOnlyField()
    date_initial = serializers.ReadOnlyField()
    date_end = serializers.ReadOnlyField()

    class Meta:
        model = ResumoDate
        fields = [
            "id",
            'trip',
            'date_initial',
            'date_end',
            'num_months',
            'money_end',
            'money_month',
        ]