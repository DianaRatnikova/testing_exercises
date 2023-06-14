from functions.level_1_7.one_avg_daily_expenses import calculate_average_daily_expenses
from functions.level_1_7.models import Expense, Currency, BankCard, ExpenseCategory
import pytest
import decimal
import datetime

@pytest.fixture
def expense1():
    return Expense(amount=decimal.Decimal('10.8'), 
                       currency=Currency("USD"), 
                       card = BankCard(last_digits='234', owner="John"), 
                       spent_in="Shop1", 
                       spent_at=datetime.datetime.now(), 
                       category=ExpenseCategory("SUPERMARKET"))

@pytest.fixture
def expense2():
    return Expense(amount=decimal.Decimal('1000.3'), 
                   currency=Currency("RUB"), 
                   card = BankCard(last_digits='777', owner="Kate"), 
                   spent_in="Shop2", 
                   spent_at=datetime.datetime.now(), 
                   category=ExpenseCategory("THEATRES_MOVIES_CULTURE"))
 