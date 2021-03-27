from django.urls import path, include
from rest_framework.routers import SimpleRouter
from .views import PerfilViajanteViewSet, TripViewSet, ResumoViewSet, ResumoDateViewSet

router = SimpleRouter()
router.register('perfil', PerfilViajanteViewSet)
router.register('trip', TripViewSet)
router.register('resumo', ResumoViewSet)
router.register('resumo_date', ResumoDateViewSet)
