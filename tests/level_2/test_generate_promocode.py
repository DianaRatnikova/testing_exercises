import random
from unittest import mock
from functions.level_2.three_promocodes import generate_promocode


#Это оч интересная функция, ннада будет подумать, как тестировать))

def test__generate_promocode_is_valid():
    with mock.patch('random.choice', return_value='A'):
        assert generate_promocode() == 'AAAAAAAA'


def test__generate_promocode_is_valid_double_random():
    with mock.patch('random.choice', return_value='bb'):
        assert generate_promocode() == 'bbbbbbbbbbbbbbbb'       


def test__generate_promocode_with_argument():
    with mock.patch('random.choice', return_value='1D'):
        assert generate_promocode(1) == '1D'           


def test__generate_promocode_with_empty_symbol():
    with mock.patch('random.choice', return_value=''):
        assert generate_promocode(1) == ''           


def test__generate_promocode_with_zero_argument():
    with mock.patch('random.choice', return_value='HELLO'):
        assert generate_promocode(0) == ''   

def test__generate_promocode_twenty_symbols():
    with mock.patch('random.choice', return_value='0'):
        assert generate_promocode(20) == '00000000000000000000'   