from rest_framework import viewsets

# Create your views here.
from .models import PerfilViajante, Trip, Resumo, ResumoDate
from .serializers import PerfilViajanteSerializer, TripSerializer, ResumoSerializer, ResumoDateSerializer


class PerfilViajanteViewSet(viewsets.ModelViewSet):
    queryset = PerfilViajante.objects.all()
    serializer_class = PerfilViajanteSerializer


class TripViewSet(viewsets.ModelViewSet):
    queryset = Trip.objects.all()
    serializer_class = TripSerializer


class ResumoViewSet(viewsets.ModelViewSet):
    queryset = Resumo.objects.all()
    serializer_class = ResumoSerializer


class ResumoDateViewSet(viewsets.ModelViewSet):
    queryset = ResumoDate.objects.all()
    serializer_class = ResumoDateSerializer