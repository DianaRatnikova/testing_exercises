from functions.level_1_5.five_replace_word import replace_word
import pytest


@pytest.mark.parametrize(
  "text, replace_from, replace_to, expected_result",
  [
    ('text_replace_1', 'replace_from_1', 'replace_to_1', 'replace_result_1'),
    ('text_replace_2', 'replace_from_1', 'replace_to_1', 'replace_result_2'),
    ('text_replace_1', 'replace_from_2', 'replace_to_1', 'replace_result_3'),
    ('text_replace_1', 'replace_from_3', 'replace_to_1', 'text_replace_1'), 
    ('text_replace_1', 'replace_from_4', 'replace_to_1', 'text_replace_1'),
    ('text_replace_1', 'replace_from_1', 'replace_from_4', 'replace_result_4')
  ]
)
def test__replace_word__is_valid(text, replace_from, replace_to, expected_result, request):
    text = request.getfixturevalue(text)
    replace_from = request.getfixturevalue(replace_from)
    replace_to = request.getfixturevalue(replace_to)
    expected_result = request.getfixturevalue(expected_result)
    assert replace_word(text, replace_from, replace_to) == expected_result


@pytest.mark.parametrize(
  "text, replace_from, replace_to, expected_error",
  [
    ('text_replace_1', 'replace_from_1', 'replace_to_2', TypeError),
    ('text_replace_1', 'replace_from_5', 'replace_to_3', AttributeError),
    ('text_replace_3', 'replace_from_1', 'replace_to_3', AttributeError),
  ]
)
def test__replace_word__errors(text, replace_from, replace_to, expected_error, request):
  text = request.getfixturevalue(text)
  replace_from = request.getfixturevalue(replace_from)
  replace_to = request.getfixturevalue(replace_to)
  with pytest.raises(expected_error):
      replace_word(text, replace_from, replace_to)


def test__replace_word__not_enough_params_typeerror(replace_to_3):
    with pytest.raises(TypeError):   
        replace_word(replace_to_3, 'bsrbg')