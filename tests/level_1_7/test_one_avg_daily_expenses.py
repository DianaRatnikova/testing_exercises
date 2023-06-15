
from functions.level_1_7.one_avg_daily_expenses import calculate_average_daily_expenses
import pytest
import decimal



def test__calculate_average_daily_expenses__is_valid(expense1, expense2):
    assert calculate_average_daily_expenses([expense1, expense2]) == decimal.Decimal('21.6')
