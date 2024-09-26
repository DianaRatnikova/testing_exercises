from functions.level_1_5.two_square_equation import solve_square_equation
import pytest


@pytest.mark.parametrize(
  "square_coefficient, linear_coefficient, const_coefficient, expected_results",
      [
      ('square_coefficient_1', 'square_coefficient_1', 'square_coefficient_1', 'square_result_1'),
      ('square_coefficient_2', 'linear_coefficient_2', 'square_coefficient_1', 'square_result_2'),
      ('square_coefficient_1', 'linear_coefficient_2', 'const_coefficient_1', 'square_result_3'),
      ('square_coefficient_1', 'linear_coefficient_2', 'square_coefficient_1', 'square_result_4'),
      ('square_coefficient_3', 'square_coefficient_1',  'const_coefficient_2', 'square_result_5'),
      ('square_coefficient_2', 'linear_coefficient_3', 'const_coefficient_3', 'square_result_6'),
      ('square_coefficient_4', 'linear_coefficient_2', 'square_coefficient_2', 'square_result_1'),
      ('square_coefficient_5', 'linear_coefficient_4', 'const_coefficient_4', 'square_result_7'),
  ]      

)
def test__solve_square_equation__is_valid(square_coefficient, linear_coefficient, const_coefficient, expected_results, request):
    square_coefficient = request.getfixturevalue(square_coefficient)
    linear_coefficient = request.getfixturevalue(linear_coefficient)
    const_coefficient = request.getfixturevalue(const_coefficient)
    expected_results = request.getfixturevalue(expected_results)
    assert solve_square_equation(square_coefficient, linear_coefficient, const_coefficient) == expected_results


def test__solve_square_equation__not_enougt_params(square_coefficient_1):
    with pytest.raises(TypeError):
        solve_square_equation(square_coefficient_1, square_coefficient_1)


def test__solve_square_equation__too_many_params(square_coefficient_2, linear_coefficient_2, square_coefficient_1):
    with pytest.raises(TypeError):
        solve_square_equation(square_coefficient_2, linear_coefficient_2, square_coefficient_1, 9)


def test__solve_square_equation__params_are_string(square_coefficient_6, linear_coefficient_5, const_coefficient_5):
    with pytest.raises(TypeError):
        solve_square_equation(square_coefficient_6, linear_coefficient_5, const_coefficient_5)


def test__solve_square_equation__params_are_lists(square_coefficient_7):
    with pytest.raises(TypeError):
        solve_square_equation(square_coefficient_7, square_coefficient_7, square_coefficient_7)
