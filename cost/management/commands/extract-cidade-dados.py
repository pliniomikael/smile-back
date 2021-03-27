from django.core.management.base import BaseCommand
from django.utils import timezone
from extractor.base import DadosCitiesExtractor


class Command(BaseCommand):
    help = 'Displays current time'

    def handle(self, *args, **kwargs):
        result = DadosCitiesExtractor()
        print(result)
