from functions.level_1_7.four_fraud import find_fraud_expenses
from functions.level_1_7.models import Expense, Currency, BankCard, ExpenseCategory
import datetime
import decimal


def test__find_fraud_expenses__empty_list():
    assert find_fraud_expenses([]) == []


def test__find_fraud_expenses__one_expense(expense_small_amount):
    assert find_fraud_expenses([expense_small_amount]) == []

def test__find_fraud_expenses__many_expenses_with_bad_spent_in(expense_small_amount):
    assert find_fraud_expenses([expense_small_amount]*10) == []

def test__find_fraud_expenses__big_amount(expense_small_amount, expense_four_big_amount):
    assert find_fraud_expenses([expense_small_amount, expense_four_big_amount]) == []   


def test__find_fraud_expenses__many_expenses(expense_spend_in_is_equal_to_spent_at):
    assert find_fraud_expenses([expense_spend_in_is_equal_to_spent_at]*3) == [expense_spend_in_is_equal_to_spent_at]*3