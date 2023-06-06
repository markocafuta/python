import pytest
import re
from flaskr.task2._braces_checker import _BracesChecker, _UnbalancedBracesError

"""
To increase readability of test method names, symbols will be used as:
    p => (
    P => )
    s => [
    S => ]
    c => {
    C => }
"""


class TestBracesChecker:
    def setup_method(self, method):
        self.__BALANCED_MESSAGE = "Braces are balanced."

    def test_given_empty_string_then_balanced(self):
        self.assert_balanced("")

    def test_given_string_with_no_braces_then_balanced(self):
        self.assert_balanced("Given text without braces")

    def test_given_P_then_raises_unbalanced_braces_error(self):
        self.assert_unbalanced("Given unbalanced ) text", "Given unbalanced )")

    def test_given_p_P_then_balanced(self):
        self.assert_balanced("() balanced")

    def test_given_p_P_p_then_raises_unbalanced_braces_error(self):
        self.assert_unbalanced("()( unbalanced", "()(")

    def test_given_p_s_P_then_raises_unbalanced_braces_error(self):
        self.assert_unbalanced("([) unbalanced", "([")

    def test_given_p_s_c_C_S_P_then_raises_unbalanced_braces_error(self):
        self.assert_balanced("([{}]) balanced")

    def assert_balanced(self, given_text):
        assert self.do_test(given_text) == self.__BALANCED_MESSAGE

    def assert_unbalanced(self, given_text, expected_output):
        with pytest.raises(_UnbalancedBracesError, match=f"{re.escape(expected_output)}$"):
            self.do_test(given_text)

    def do_test(self, given_text):
        return _BracesChecker(given_text).check_if_balanced()
