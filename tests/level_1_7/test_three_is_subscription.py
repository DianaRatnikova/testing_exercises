from functions.level_1_7.three_is_subscription import is_subscription
from functions.level_1_7.models import Expense, Currency, BankCard, ExpenseCategory
import datetime
import decimal


def test__is_subscription__short_history():
    expense1 = Expense(
        amount=decimal.Decimal('10.8'), 
        currency=Currency("USD"), 
        card = BankCard(last_digits='234', owner="John"), 
        spent_in="green apple", 
        spent_at=datetime.datetime(2005, 1, 14),
        category=ExpenseCategory("SUPERMARKET"))
    assert is_subscription(expense1, [expense1, expense1]) == False


def test__is_subscription__long_history():
    expense1 = Expense(
        amount=decimal.Decimal('10.8'), 
        currency=Currency("USD"),
        card = BankCard(last_digits='234', owner="John"),
        spent_in="green apple",
        spent_at=datetime.datetime(2005, 1, 14),
        category=ExpenseCategory("SUPERMARKET"))
    assert is_subscription(expense1, [expense1, expense1, expense1, expense1, expense1]) == False


def test__is_subscription__true():
   expense1 = Expense(
       amount=decimal.Decimal('10.8'),
       currency=Currency("USD"),
       card = BankCard(last_digits='234', owner="John"),
       spent_in="green apple",
       spent_at=datetime.datetime(2005, 1, 14),
       category=ExpenseCategory("SUPERMARKET"))
   
   expense1_1 = Expense(
       amount=decimal.Decimal('10.8'),
       currency=Currency("USD"),
       card = BankCard(last_digits='234', owner="John"),
       spent_in="green apple",
       spent_at=datetime.datetime(2005, 2, 14),
       category=ExpenseCategory("SUPERMARKET"))
   
   expense1_2 = Expense(
       amount=decimal.Decimal('10.8'),
       currency=Currency("USD"),
       card = BankCard(last_digits='234', owner="John"),
       spent_in="green apple",
       spent_at=datetime.datetime(2005, 3, 14),
       category=ExpenseCategory("SUPERMARKET"))
   
   expense1_3 = Expense(
       amount=decimal.Decimal('10.8'),
       currency=Currency("USD"),
       card = BankCard(last_digits='234', owner="John"),
       spent_in="green apple",
       spent_at=datetime.datetime(2005, 4, 14),
       category=ExpenseCategory("SUPERMARKET"))
   
   assert is_subscription(expense1, [expense1, expense1_1, expense1_2, expense1_3]) == True