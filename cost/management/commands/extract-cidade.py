from django.core.management.base import BaseCommand
from django.utils import timezone
from extractor.base import CitiesExtractor


class Command(BaseCommand):
    help = 'Displays current time'

    def handle(self, *args, **kwargs):
        url = 'https://pt.numbeo.com/custo-de-vida/pa%C3%ADs/Brasil'
        result = CitiesExtractor(url)
        print(result)
