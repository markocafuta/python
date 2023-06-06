import time

import pytest

from flaskr.task3 import task3


def assert_cached_result():
    assert task3.cached(1, 2, a=3) == 3


@pytest.fixture(autouse=True)
def reset_cache():
    task3.cached.reset_decorator()


def test_given_no_spy_func_when_cached_func_called_then_return_result_without_error():
    assert_cached_result()


def assert_calls_count(test_func, actual_calls_count):
    call_counter = 0

    def record_call():
        nonlocal call_counter
        call_counter += 1

    task3._spy = record_call
    test_func()
    assert call_counter == actual_calls_count


def test_when_cached_func_called_11_times_then_2_actual_calls():
    def do_test():
        for i in range(11):
            assert_cached_result()

    assert_calls_count(do_test, 2)


def test_when_cached_func_called_2_times_in_interval_more_then_5_then_2_actual_calls(monkeypatch):
    def do_test():
        def epoch_1_sec():
            return 1

        def epoch_302_sec():
            return 302

        monkeypatch.setattr(time, 'time', epoch_1_sec)
        assert_cached_result()
        monkeypatch.setattr(time, 'time', epoch_302_sec)
        assert_cached_result()

    assert_calls_count(do_test, 2)
