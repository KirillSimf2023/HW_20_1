# management/commands/fill.py
from django.core.management import BaseCommand

from catalog.models import Product, Category
import json


class Command(BaseCommand):

    def handle(self, *args, **options):
        # очистка таблицы
        Product.objects.all().delete()
        Category.objects.all().delete()

        with open('data_category.json', encoding='utf-8') as f:
            data = json.load(f)

        for item in data:
            print(item['fields'])
            Category.objects.create(**item['fields'])

        with open('data_product.json', encoding='utf-8') as f:
            data = json.load(f)

        for item in data:
            print(item['fields'])
            Product.objects.create(**item['fields'])

