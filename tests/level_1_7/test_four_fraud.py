from functions.level_1_7.four_fraud import find_fraud_expenses
from functions.level_1_7.models import Expense, Currency, BankCard, ExpenseCategory
import datetime
import decimal


def test__find_fraud_expenses__empty_list():
    assert find_fraud_expenses([]) == []


def test__find_fraud_expenses__one_expense():
    expense1 = Expense(
        amount=decimal.Decimal('10.8'), 
        currency=Currency("USD"), 
        card = BankCard(last_digits='234', owner="John"), 
        spent_in="green apple", 
        spent_at=datetime.datetime(2005, 1, 14),
        category=ExpenseCategory("SUPERMARKET"))
    assert find_fraud_expenses([expense1]) == []


def test__find_fraud_expenses__big_amount():
    expense1 = Expense(
        amount=decimal.Decimal('7000001'), 
        currency=Currency("USD"), 
        card = BankCard(last_digits='234', owner="John"), 
        spent_in="green apple", 
        spent_at=datetime.datetime(2005, 1, 14),
        category=ExpenseCategory("SUPERMARKET"))
    
    expense2 = Expense(
        amount=decimal.Decimal('50001'), 
        currency=Currency("USD"), 
        card = BankCard(last_digits='234', owner="John"), 
        spent_in="green apple", 
        spent_at=datetime.datetime(2005, 1, 14),
        category=ExpenseCategory("SUPERMARKET"))
    assert find_fraud_expenses([expense1, expense2]) == []   