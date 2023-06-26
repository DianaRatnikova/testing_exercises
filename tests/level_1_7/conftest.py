import pytest
from functions.level_1_7.models import Expense, Currency, BankCard, ExpenseCategory
import pytest
import decimal
import datetime


@pytest.fixture
def expense_small_amount():
    return Expense(
            amount=decimal.Decimal('10.8'), 
            currency=Currency("USD"), 
            card = BankCard(last_digits='234', owner="John"), 
            spent_in="green apple", 
            spent_at=datetime.datetime(2005, 1, 14),
            category=ExpenseCategory("SUPERMARKET")
        )


@pytest.fixture
def expense_four_big_amount():
    return Expense(
            amount=decimal.Decimal('50000'), 
            currency=Currency("USD"), 
            card = BankCard(last_digits='234', owner="John"), 
            spent_in="green apple", 
            spent_at=datetime.datetime(2005, 1, 14),
            category=ExpenseCategory("SUPERMARKET")
        )


@pytest.fixture
def expense_spend_in_is_equal_to_spent_at():
    return Expense(
            amount=decimal.Decimal('500'), 
            currency=Currency("USD"), 
            card = BankCard(last_digits='234', owner="John"), 
            spent_in=datetime.datetime(2005, 2, 14), 
            spent_at=datetime.datetime(2005, 2, 14),
            category=ExpenseCategory("SUPERMARKET")
        )