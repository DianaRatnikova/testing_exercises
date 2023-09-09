import pytest

@pytest.fixture
def text_replace_1():
     return 'one two three four'

@pytest.fixture
def text_replace_2():
     return 'one two three Two four'

@pytest.fixture
def text_replace_3():
     return 123314


@pytest.fixture
def replace_from_1():
     return 'two'

@pytest.fixture
def replace_from_2():
     return  'TWo'

@pytest.fixture
def replace_from_3():
     return  '1234'

@pytest.fixture
def replace_from_4():
     return  ''

@pytest.fixture
def replace_from_5():
     return  2

@pytest.fixture
def replace_to_1():
     return  'replace_to'

@pytest.fixture
def replace_to_2():
     return  123

@pytest.fixture
def replace_to_3():
     return  '123'

@pytest.fixture
def replace_result_1():
     return  'one replace_to three four'

@pytest.fixture
def replace_result_2():
     return  'one replace_to three replace_to four'

@pytest.fixture
def replace_result_3():
     return  'one replace_to three four'

@pytest.fixture
def replace_result_4():
     return  'one  three four'
