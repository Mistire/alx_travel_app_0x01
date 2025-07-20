from django.core.management.base import BaseCommand
from listings.models import Listing
from faker import Faker
import random

class Command(BaseCommand):
    help = 'Seed the database with Listings'

    def handle(self, *args, **kwargs):
        fake = Faker()
        for _ in range(10):
            Listing.objects.create(
                title=fake.catch_phrase(),
                description=fake.text(),
                location=fake.city(),
                price_per_night=random.uniform(20, 300),
                available=True
            )
        self.stdout.write(self.style.SUCCESS('Successfully seeded listings'))
