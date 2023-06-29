from functions.level_2.one_brackets import delete_remove_brackets_quotes
import pytest


# убрала неуниверсальную фикстуру
def test__delete_remove_brackets_quotes__function_in_return_of_result(name_with_brakets):
    result = name_with_brakets[2:len(name_with_brakets) - 2]
    assert delete_remove_brackets_quotes(name_with_brakets) == result


def test__delete_remove_brackets_quotes__result2_is_string(name_with_brakets):
    assert delete_remove_brackets_quotes(name_with_brakets) == "Something"


# Два теста выше оставила просто на проверку, хотя понимаю, что параметрайз
# и эти две функции взаимозаменяемы.



# Вопрос: хочу вместо first_return_from_delete_remove_brackets_quotes использовать что-то вроде
# прямого указания среза name_with_brakets[2:len(name_with_brakets) - 2], но как записать, и возможно ли?
# так-то выходит, что эта фикстура неуниверсальная, используется только один раз (с учётом, что тесты в стр 5-12 я уберу)
@pytest.mark.parametrize(
    "name, expected_result",
    [
        ('name_with_brakets', 'first_return_from_delete_remove_brackets_quotes'),
        ('name_with_brakets', "Something"),
    ]
)
def test__delete_remove_brackets_quotes__is_valid(name, expected_result, request):
    name = request.getfixturevalue(name)
   # expected_result = request.getfixturevalue(expected_result)
    assert delete_remove_brackets_quotes(name) == expected_result