import pytest
from flaskr.task1._full_name_joiner import _FullNameJoiner


class TestFullNameJoiner:
    def setup_method(self, method):
        self.full_name_joiner = _FullNameJoiner()

    def test_given_empty_input_then_return_empty_full_names(self):
        self.__given_names = {}

        self.__expected_full_names = {
            'full_names': []
        }

        self.__assert_test()

    def test_given_empty_first_names_then_return_last_names_with_unpaired_first_name(self):
        self.__given_names = {
            "last_names": [
                ["Anderson", "4321"],
                ["Smith", "1234"]
            ]
        }

        self.__expected_full_names = {
            'full_names': [
                ["unpaired", "Smith", "1234"],
                ["unpaired", "Anderson", "4321"],
            ]
        }

        self.__assert_test()

    def test_given_empty_last_names_then_return_first_names_with_unpaired_last_names(self):
        self.__given_names = {
            "first_names": [
                ["John", "4321"],
                ["Adam", "1234"]
            ]
        }

        self.__expected_full_names = {
            'full_names': [
                ["Adam", "unpaired", "1234"],
                ["John", "unpaired", "4321"],
            ]
        }

        self.__assert_test()

    def test_given_first_names_and_last_names_then_return_full_names(self):
        self.__given_names = {
            "first_names": [
                ["John", "4321"],
                ["Adam", "1234"],
                ["Tom", "2222"]
            ],
            "last_names": [
                ["Anderson", "4321"],
                ["Smith", "1234"],
                ["Man", "3333"]
            ]
        }

        self.__expected_full_names = {
            'full_names': [
                ["Adam", "Smith", "1234"],
                ["Tom", "unpaired", "2222"],
                ["unpaired", "Man", "3333"],
                ["John", "Anderson", "4321"],
            ]
        }

        self.__assert_test()

    def test_given_invalid_first_names_rasie_value_error(self):
        self.__given_names = {
            "first_names": [
                ["John", "4321"],
                ["Adam"],
                ["Tom", "2222"]
            ],
            "last_names": [
                ["Anderson", "4321"],
                ["Smith", "1234"],
                ["Man", "3333"]
            ]
        }

        with pytest.raises(ValueError, match="Invalid item: \['Adam'\]. Name or ID missing!"):
            self.full_name_joiner.join_names(self.__given_names)

    def test_given_non_numeric_id_in_first_names_rasie_value_error(self):
        self.__given_names = {
            "first_names": [
                ["John", "4321"],
                ["Adam", "12e4"],
                ["Tom", "2222"]
            ],
            "last_names": [
                ["Anderson", "4321"],
                ["Smith", "1234"],
                ["Man", "3333"]
            ]
        }

        with pytest.raises(ValueError, match=r"Invalid item: \['Adam', '12e4'\]. ID not numeric!"):
            self.full_name_joiner.join_names(self.__given_names)

    def test_given_invalid_last_names_rasie_value_error(self):
        self.__given_names = {
            "first_names": [
                ["John", "4321"],
                ["Adam", "1234"],
                ["Tom", "2222"]
            ],
            "last_names": [
                ["Anderson", "4321"],
                ["Smith", "1234"],
                ["3333"]
            ]
        }

        with pytest.raises(ValueError, match=r"Invalid item: \['3333'\]. Name or ID missing!"):
            self.full_name_joiner.join_names(self.__given_names)

    def test_given_non_numeric_id_in_last_names_rasie_value_error(self):
        self.__given_names = {
            "first_names": [
                ["John", "4321"],
                ["Adam", "1234"],
                ["Tom", "2222"]
            ],
            "last_names": [
                ["Anderson", "4321"],
                ["Smith", "1234"],
                ["Man", "33r3"]
            ]
        }

        with pytest.raises(ValueError, match=r"Invalid item: \['Man', '33r3'\]. ID not numeric!"):
            self.full_name_joiner.join_names(self.__given_names)

    def __assert_test(self):
        assert self.full_name_joiner.join_names(self.__given_names) == self.__expected_full_names
