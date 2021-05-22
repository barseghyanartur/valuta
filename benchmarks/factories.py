from faker import Faker
from constants import URLS_COUNT

__all__ = (
    'CURRENCIES',
)


fake = Faker()
fake.seed(URLS_COUNT)


CURRENCIES = [fake.currency_code() for _ in range(URLS_COUNT)]
