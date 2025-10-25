from django.core.management.base import BaseCommand
from listings.models import Listing
from faker import Faker
import random

class Command(BaseCommand):
    helper = 'help seed the database for testing and development'

    def handle(self, *args, **options):
        fake = Faker()
        self.stdout.write('Seeding database....Processing')

        Listing.objects.all().delete()

        for _ in range(100):
            Listing.objects.create(
                property_id = fake.uuid4(),
                host_id = fake.uuid4(),
                name = fake.text(),
                description = fake.text(),
                location = fake.city(),
                pricepernight = fake.pydecimal(left_digits=5, right_digits=2, positive=True),
                created_at = fake.date_time_between(start_date='-2y', end_date='now'),
                updated_at = fake.date_time_between(start_date='-2y', end_date='now')
            )
        self.stdout.write(self.style.SUCCESS('successfully seeded the database with 100 listings'))