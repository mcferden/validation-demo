from dataclasses import dataclass
from datetime import date
from decimal import Decimal
from typing import List, Optional


@dataclass
class Transaction:
    id: int
    amount: Decimal


@dataclass
class BaseUser:
    email: str
    first_name: Optional[str]
    last_name: Optional[str]
    birth_date: Optional[date]


@dataclass
class User(BaseUser):
    id: int
    transactions: List[Transaction]


@dataclass
class UserCreate(BaseUser):
    password: str
