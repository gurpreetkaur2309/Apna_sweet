# Apna/management/commands/generate_fake_products.py
from django.core.management.base import BaseCommand
from faker import Faker
from Apna.models import Product
import random

class Command(BaseCommand):
    help = 'Generate fake data for Product model'

    def handle(self, *args, **kwargs):
        fake = Faker()

        CATEGORY_CHOICES = ['S', 'N', 'M', 'B']
        BRAND_CHOICES = ['J', 'A', 'S', 'M']

        sweets = {
            "Gulab Jamun": "gulab_jamun.png",
            "Rasgulla": "rasgulla.png",
            "Ladoo": "ladoo.png",
            "Barfi": "barfi.png",
            "Jalebi": "jalebi.png"
        }
        namkeens = {
            "Bhujia": "bhujia.png",
            "Chakli": "chakli.png",
            "Namkeen Mixture": "bhujia.png",  # Reusing image for variety
            "Sev": "bhujia.png"  # Reusing image for variety
        }
        meals = {
            "Plain Roti": "roti.png",
            "Butter Roti": "roti.png",
            "Garlic Roti": "roti.png",
            "Stuffed Roti": "roti.png",
            "Spicy Roti": "roti.png"
        }
        bakeries = {
            "Cake": "cake.png",
            "Chocolate Cake": "cake.png",
            "Vanilla Cake": "cake.png",
            "Strawberry Cake": "cake.png",
            "Black Forest Cake": "cake.png"
        }

        for _ in range(100):  # Generate 100 fake products
            category = random.choice(CATEGORY_CHOICES)
            if category == 'S':
                item_name, item_image = random.choice(list(sweets.items()))
            elif category == 'N':
                item_name, item_image = random.choice(list(namkeens.items()))
            elif category == 'M':
                item_name, item_image = random.choice(list(meals.items()))
            elif category == 'B':
                item_name, item_image = random.choice(list(bakeries.items()))

            Product.objects.create(
                item_name=item_name,
                item_price=round(random.uniform(10.0, 100.0), 2),
                item_brand=random.choice(BRAND_CHOICES),
                item_category=category,
                item_image=f'product/{item_image}'  # Use the corresponding image
            )

        self.stdout.write(self.style.SUCCESS('Successfully generated fake products'))
