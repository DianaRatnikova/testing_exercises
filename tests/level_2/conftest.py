import pytest
from functions.level_2.two_students import Student


@pytest.fixture
def name_with_brakets():
    return("{ Something }")

# хочу продублировать функционал ретёрна функции, но если описывать смысл, то выходит оч длинное название
@pytest.fixture
def first_return_from_delete_remove_brackets_quotes(name_with_brakets):
   return name_with_brakets[2:len(name_with_brakets) - 2]

@pytest.fixture
def name2():
    return("{ Something }")


@pytest.fixture
def student1():
    return Student("Diana", "Ratnikova", "@winterlich_weiss")

@pytest.fixture
def student2():
    return Student("Name", "Last Name", "@nickname")

@pytest.fixture
def student3():
    return Student("wrtgshn", "athbgfs", "nickname")

@pytest.fixture
def students(student1, student2, student3):
    return [student1, student2, student3]

@pytest.fixture
def telegram_username1():
    return "winterlich_weiss"

@pytest.fixture
def telegram_username2():
    return "wshgfhnjtnhg"
