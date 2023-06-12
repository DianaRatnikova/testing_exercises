from functions.level_1.five_title import change_copy_item
import pytest


@pytest.mark.parametrize(
    "title, max_main_item_title_length, expected_result",
    [
        ('title_1', 100, 'copy_title_1'),
        ('title_1', 10,  'title_1'),
        ('title_2', 100, 'copy_title_2'),
        ('title_3', 100, 'copy_title_3'),
        ('title_4', 100, 'copy_title_4'),
    ]
)      
def test__change_copy_item__is_valid(title, max_main_item_title_length, expected_result, request):
    title = request.getfixturevalue(title)
    expected_result = request.getfixturevalue(expected_result)
    assert change_copy_item(title, max_main_item_title_length) == expected_result
