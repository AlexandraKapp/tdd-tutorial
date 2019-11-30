import pytest
from my_greetings import greetings
from mock import Mock, patch
import os

@pytest.fixture
def mocked_person():
    """Mock a class "Person" with attribute firstname and nationality.
    """
    mocked_person = Mock()
    mocked_person.firstname = "Ada"
    mocked_person.nationality = "German"
    return mocked_person

@pytest.fixture
def mocked_morning():
    """Mock a function, that returns the current daytime.
    """
    mocked_daytime = Mock(return_value="morning")
    return mocked_daytime


def test_greet_in_german_with_name_in_the_morning(mocked_person, mocked_morning):
    daytime = mocked_morning()
    greeting = greetings.greet(mocked_person, daytime)
    expected_greeting = "Guten Morgen, Ada!"
    
    assert expected_greeting == greeting
    assert mocked_morning.called
    assert mocked_morning.call_count == 1
    assert isinstance(expected_greeting, str)
