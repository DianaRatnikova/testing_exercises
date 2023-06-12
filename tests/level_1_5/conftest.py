import pytest

# test_solve_square_equation

@pytest.fixture
def square_coefficient_1():
    return 0

@pytest.fixture
def square_coefficient_2():
    return 5

@pytest.fixture
def square_coefficient_3():
    return 4

@pytest.fixture
def square_coefficient_4():
    return 1

@pytest.fixture
def square_coefficient_5():
    return 1.1

@pytest.fixture
def square_coefficient_6():
    return 'a'

@pytest.fixture
def square_coefficient_7():
    return [0]

@pytest.fixture
def linear_coefficient_2():
    return 2

@pytest.fixture
def linear_coefficient_3():
    return 3

@pytest.fixture
def linear_coefficient_4():
    return 2.2

@pytest.fixture
def linear_coefficient_5():
    return 'b'

@pytest.fixture
def const_coefficient_1():
    return 10

@pytest.fixture
def const_coefficient_2():
    return -16

@pytest.fixture
def const_coefficient_3():
    return -26

@pytest.fixture
def const_coefficient_4():
    return -5.5

@pytest.fixture
def const_coefficient_5():
    return 'c'


@pytest.fixture
def square_result_1():
    return (None, None)

@pytest.fixture
def square_result_2():
    return (-0.4, 0.0)

@pytest.fixture
def square_result_3():
    return (-5.0, None)

@pytest.fixture
def square_result_4():
    return (0.0, None)

@pytest.fixture
def square_result_5():
    return (-2.0, 2.0)

@pytest.fixture
def square_result_6():
    return  (-2.6, 2.0)

@pytest.fixture
def square_result_7():
    return (-3.449489742783178, 1.4494897427831779)

