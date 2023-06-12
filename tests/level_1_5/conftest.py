import pytest


# test_one_median

@pytest.fixture
def items_empty():
    return ""

@pytest.fixture
def result_none():
    return None

@pytest.fixture
def items_1():
    return [2, 1, 5]

@pytest.fixture
def items_2():
    return [-2, -1, 5]

@pytest.fixture
def result_1_2():
    return 5

@pytest.fixture
def items_3():
    return [2, 1, 3, 9, 10]

@pytest.fixture
def items_4():
    return [2, 1, 1, 1, 3, 3, 2, 9, 9, 3, 9, 10]

@pytest.fixture
def result_3_4():
    return 9

@pytest.fixture
def items_5():
    return [0.6, 99.4, 13.2]

@pytest.fixture
def result_5():
    return 13.2

@pytest.fixture
def items_error_1():
    return 0

@pytest.fixture
def items_error_2():
    return [2, 1, 3, 9]

@pytest.fixture
def items_error_3():
    return 1
