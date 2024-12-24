from faker import Faker
import random

faker = Faker()

def fetch_leads():
    return {
        "name": faker.name(),
        "email": faker.email(),
        "lead_source": random.choice(["HubSpot", "Google Ads", "Facebook"]),
    }
