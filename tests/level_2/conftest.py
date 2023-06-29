import pytest
from functions.level_2.two_students import Student


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
