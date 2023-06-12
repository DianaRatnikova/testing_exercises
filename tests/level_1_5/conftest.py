import pytest


# test_four_checks

@pytest.fixture
def text_1():
    return 'g1 b1 g2 b2 g3 b3 '

@pytest.fixture
def text_2():
    return 'g0 b0 g0 b0 g3 b3 '

@pytest.fixture
def text_3():
    return 'g1 b2 g0 b0 g3 b3 '

@pytest.fixture
def text_4():
    return 'g1 b2 g0 b0 g3 b3 g4 b4'

@pytest.fixture
def text_5():
    return '1 2'

@pytest.fixture
def text_6():
    return 'g0 b0 g0 b0 g0 b3 g4 b4'

@pytest.fixture
def text_7():
    return 'g0 b0 g3 b3 g4 b4'

@pytest.fixture
def text_8():
    return 'g0 b0 g3  b3 g4 b4'

@pytest.fixture
def text_9():
    return ''

@pytest.fixture
def text_10():
    return 'one two'

@pytest.fixture
def text_11():
    return 123

@pytest.fixture
def good_words_1():
    return {'g1', 'g2'}

@pytest.fixture
def good_words_2():
    return {'g1', 'g2', 'g3'}

@pytest.fixture
def good_words_3():
    return '5 6 7 4'

@pytest.fixture
def good_words_3():
    return {''}

@pytest.fixture
def good_words_4():
    return 'one'


@pytest.fixture
def bad_words_1():
    return {'b1', 'b2'}

@pytest.fixture
def bad_words_2():
    return '2'

@pytest.fixture
def bad_words_3():
    return 'two'
