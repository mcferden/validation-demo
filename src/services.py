from dataclasses import asdict
import random
from decimal import Decimal

from entities import Transaction, User, UserCreate


class UsersService:
    def create_user(self, user: UserCreate) -> User:
        user_data = asdict(user)
        user_data.pop('password')
        return User(
            **user_data,
            id=random.randint(1, 100),
            transactions=[
                Transaction(id=1, amount=Decimal(1000)),
                Transaction(id=2, amount=Decimal(2000)),
                Transaction(id=3, amount=Decimal(3000)),
            ],
        )
