from functions.level_1_7.two_expense_categorizer import guess_expense_category, is_string_contains_trigger
from functions.level_1_7.models import  ExpenseCategory
import pytest



def test__guess_expense_category__bar_restaurant(expense1):
    assert guess_expense_category(expense1) == ExpenseCategory.BAR_RESTAURANT

def test__guess_expense_category__bar_restaurant1(expense3):
    assert guess_expense_category(expense3) == ExpenseCategory.BAR_RESTAURANT


def test__guess_expense_category__bar_restaurant(expense2):
    assert guess_expense_category(expense2) == None


@pytest.mark.parametrize(
"original_string, trigger, expected_result",
[
    ('julius', 'julius', True),
    ('JulIUS', 'julius', True),
    (' julius', 'julius', True),
    (',julius', 'julius', True),
    ('..,/.julius', 'julius', True),
    ('julius..,/.', 'julius', True),
    ('julius..,/.FFFF', 'julius',  True),
    ('', 'julius', False), 
    ('..,/.julius', '...julius', False),
    ('htg.julius.52t4w5.,/.FFFF', '-julius-', False) 
]
)
def  test__is_string_contains_trigger__is_valid(original_string, trigger, expected_result):
    assert is_string_contains_trigger(original_string, trigger) == expected_result   