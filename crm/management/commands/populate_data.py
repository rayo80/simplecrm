from django.core.management.base import BaseCommand
from faker import Faker
from crm.models import User, Company, Customer, Interaction
import random
from datetime import timezone


class Command(BaseCommand):
    help = 'Populates the database with fake data'

    def handle(self, *args, **options):
        fake = Faker()

        # Create 3 users
        users = []
        for _ in range(3):
            user = User.objects.create_user(
                username=fake.user_name(),
                email=fake.email(),
                password='password123'  # You should use a more secure password in production
            )
            users.append(user)

        # Create some companies
        companies = []
        for _ in range(10):
            company = Company.objects.create(
                name=fake.company()
            )
            companies.append(company)

        # Create 100 customers (it was 1000 but is to much for test with sqlite)
        customers = []
        for _ in range(100):
            customer = Customer.objects.create(
                first_name=fake.first_name(),
                last_name=fake.last_name(),
                birth_date=fake.date_of_birth(minimum_age=18, maximum_age=65),
                company=random.choice(companies),
                sales_representative=random.choice(users)
            )
            customers.append(customer)

        # Create 30 interactions per customer (it was 500 but is to much for test with sqlite)
        interaction_types = ['Call', 'Email', 'SMS', 'Facebook', 'Twitter']
        for customer in customers:
            print(f"Creating interactions for customer: {customer.first_name} {customer.last_name}")
            for _ in range(30):
                interaction = Interaction.objects.create(
                    customer=customer,
                    interaction_type=random.choice(interaction_types),
                    interaction_date=fake.date_time_between(start_date='-1y', end_date='now', tzinfo=timezone.utc)
                )

        self.stdout.write(self.style.SUCCESS('Successfully populated the database with fake data'))
