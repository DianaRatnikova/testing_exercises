from functions.level_1_7.one_avg_daily_expenses import calculate_average_daily_expenses
from functions.level_1_7.models import Expense, Currency, BankCard, ExpenseCategory
import pytest
import decimal
import datetime


@pytest.fixture
def amount():
    return decimal.Decimal('10.8')


@pytest.fixture
def card():
    return BankCard(last_digits='234', owner="John")

@pytest.fixture
def spent_at():
    return datetime.datetime.now()

@pytest.fixture
def julius():
    return "julius"

@pytest.fixture
def expense1(amount, card, spent_at, julius):
    return Expense(amount=amount, 
                       currency=Currency("USD"), 
                       card = card, 
                       spent_in=julius, 
                       spent_at=spent_at, 
                       category=ExpenseCategory("SUPERMARKET"))

@pytest.fixture
def expense2(amount, card, spent_at):
    return Expense(amount=amount, 
                   currency=Currency("RUB"), 
                   card = card, 
                   spent_in="Shop2", 
                   spent_at=spent_at, 
                   category=ExpenseCategory("THEATRES_MOVIES_CULTURE"))