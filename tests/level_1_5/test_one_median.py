from functions.level_1_5.one_median import get_median_value
import pytest


@pytest.mark.parametrize(
  "items, expected_result",
  [
      ('items_empty', 'result_none'),
      ('items_1', 'result_1_2'),
      ('items_2', 'result_1_2'),
      ('items_3', 'result_3_4'),
      ('items_4', 'result_3_4'),
      ('items_5', 'result_5')
  ]      
)
def test__get_median__is_valid(items, expected_result, request):
    items = request.getfixturevalue(items)
    expected_result = request.getfixturevalue(expected_result)
    assert get_median_value(items) is expected_result


@pytest.mark.parametrize(
  "items, expected_error, items_need",
  [
       ('items_error_1', TypeError, False),
       ('items_error_2', IndexError, True),
       ('items_error_3', TypeError, True)
  ]
)
def test__get_median_value__errors(items, expected_error, items_need, request):
    items = request.getfixturevalue(items)
    with pytest.raises(expected_error):
        if items_need:
            get_median_value(items)
        else:
            get_median_value()
