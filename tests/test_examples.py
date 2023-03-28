import logging
from unittest.mock import patch, MagicMock
from mysite.myapp.views import views

logger = logging.getLogger(__name__)

def test_add_two_numbers_successfully():
    actual_result = views.sample_function_add_two_numbers(2, 5)
    expected_result = 7

    assert actual_result == expected_result

def test_add_two_numbers_negative_test():
    actual_result = views.sample_function_add_two_numbers(2, 5)
    bad_result = 4

    assert actual_result != bad_result

@patch('mysite.myapp.views.views.sample_function_add_two_numbers', MagicMock(return_value=7))
def test_patch_function_call():
    actual_result = views.sample_function_add_two_numbers_then_triple_it(2, 5)
    expected_result = 21

    assert actual_result == expected_result
