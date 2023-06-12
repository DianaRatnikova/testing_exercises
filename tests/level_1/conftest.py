import pytest
import datetime



@pytest.fixture
def time_str_19_55():
    return "19:55"

@pytest.fixture
def hour_str_19_55(time_str_19_55):
   return int(time_str_19_55.strip().split(":")[0])

@pytest.fixture
def minute_str_19_55(time_str_19_55):
   return int(time_str_19_55.strip().split(":")[1])

@pytest.fixture
def date_str_tomorrow():
    return "tomorrow"

@pytest.fixture
def date_str_random():
    return "gedsf878iukf"

@pytest.fixture
def time_int_random():
    return 1234

@pytest.fixture
def expected_result_19_55_tomorrow(hour_str_19_55, minute_str_19_55): 
    return datetime.datetime(datetime.date.today().year,
                             datetime.date.today().month,
                             datetime.date.today().day+1, 
                             hour_str_19_55, 
                             minute_str_19_55)



@pytest.fixture
def expected_result_19_55_today(hour_str_19_55, minute_str_19_55): 
    return datetime.datetime(datetime.date.today().year,
                             datetime.date.today().month,
                             datetime.date.today().day, 
                             hour_str_19_55, 
                             minute_str_19_55)

@pytest.fixture()
def verb_male():
    yield "verb_male"

@pytest.fixture()
def verb_female():
    yield "verb_female"


@pytest.fixture
def gender_male():
    return "male"

@pytest.fixture
def gender_female():
    return "female"

# НЫТЬЁ: хочу, чтобы было так: один файл с тестом - один конфтест.
# уже сейчас в одном конфтесте неудобно искать нужные фикстуры.
# пишу комменты, чтобы хоть как-то их различать. И что вы мне сделаете)))

# FOR test_five_title
@pytest.fixture
def random_symbols():
    return "4w5rgt"


@pytest.fixture
def title_1():
    return 'THIS IS TITLE'

@pytest.fixture
def copy_title_1(title_1):
    return "Copy of " + title_1

@pytest.fixture
def digit_for_title():
    return 17

@pytest.fixture
def title_2(digit_for_title):
    return 'Copy of something(' + str(digit_for_title) + ')'

@pytest.fixture
def copy_title_2(digit_for_title):
    return 'Copy of (' + str(digit_for_title + 1) + ')'

@pytest.fixture
def title_3(digit_for_title):
    return 'Copy of something (' + str(digit_for_title) + ')'

@pytest.fixture
def copy_title_3(digit_for_title):
    return 'Copy of something (' + str(digit_for_title + 1) + ')'

@pytest.fixture
def not_digit_for_title():
    return '1fvd7'

# Вопрос: есть ли варианты как-то оптимизировать постоянное дублирование 
# очень похожих по смыслу фикстур?
# title_3 и title_4 здесь практически одинаковы(
@pytest.fixture
def title_4(not_digit_for_title):
    return 'Copy of something(' + str(not_digit_for_title) + ')'

@pytest.fixture
def copy_title_4(not_digit_for_title):
    return 'Copy of something(' + str(not_digit_for_title) + ') (2)'