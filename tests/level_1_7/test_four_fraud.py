from functions.level_1_7.four_fraud import find_fraud_expenses
from functions.level_1_7.models import Expense, Currency, BankCard, ExpenseCategory
import datetime
import decimal


def test__find_fraud_expenses__empty_list():
    assert find_fraud_expenses([]) == []


def test__find_fraud_expenses__one_expense(expense_four_1):
    assert find_fraud_expenses([expense_four_1]) == []

def test__find_fraud_expenses__many_expenses_with_bad_spent_in(expense_four_1):
    assert find_fraud_expenses([expense_four_1]*10) == []

def test__find_fraud_expenses__big_amount(expense_four_1, expense_four_2):
    assert find_fraud_expenses([expense_four_1, expense_four_2]) == []   


def test__find_fraud_expenses__many_expenses(expense_four_3):
    assert find_fraud_expenses([expense_four_3]*3) == [expense_four_3]*3