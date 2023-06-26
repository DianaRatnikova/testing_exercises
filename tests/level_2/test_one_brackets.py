from functions.level_2.one_brackets import delete_remove_brackets_quotes
import pytest



def test__delete_remove_brackets_quotes__function_in_return_of_result(name_with_brakets, result1):
    assert delete_remove_brackets_quotes(name_with_brakets) == result1

def test__delete_remove_brackets_quotes__result2_is_string(name_with_brakets, result2):
    assert delete_remove_brackets_quotes(name_with_brakets) == result2

# Вопрос:
# Похоже, мне нужны примеры грамотного использования фикстур в параметрайзах.
# Применила самый очевидный мне вариант в комментах ниже:
# Параметрайз здесь не видит файл конфтест.
# А если переношу фикстуры в текущий файл, жалуется, что name - это функция, 
# над которой нельзя производить действия как со строкой

@pytest.mark.parametrize(
    "name, expected_result",
    [
        ('name_with_brakets', 'result1'),
        ('name_with_brakets', 'result2'),
    ]
)
def test__delete_remove_brackets_quotes__is_valid(name, expected_result, request):
    name = request.getfixturevalue(name)
    expected_result = request.getfixturevalue(expected_result)
    assert delete_remove_brackets_quotes(name) == expected_result