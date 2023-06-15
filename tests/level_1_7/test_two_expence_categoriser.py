from functions.level_1_7.two_expense_categorizer import guess_expense_category, is_string_contains_trigger
from functions.level_1_7.models import  ExpenseCategory
import pytest



def test__guess_expense_category__bar_restaurant(expense1):
    assert guess_expense_category(expense1) == ExpenseCategory.BAR_RESTAURANT


def test__guess_expense_category__bar_restaurant(expense2):
    assert guess_expense_category(expense2) == None


def test__is_string_contains_trigger__is_valid(julius, request):
    julius = request.getfixturevalue(julius)
    assert is_string_contains_trigger(julius, julius) == True