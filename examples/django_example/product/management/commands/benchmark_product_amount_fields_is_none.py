from django.core.management.base import BaseCommand

from factories import ProductFactory
from product.models import ProductProxyAmountFieldsIsNone


class Command(BaseCommand):
    def handle(self, *args, **options):
        products = ProductFactory.create_batch(100)
        for p in products:
            product = ProductProxyAmountFieldsIsNone.objects.get(id=p.id)
            product.price_in_currency_units()
            product.price_with_tax_in_currency_units()
