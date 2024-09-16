import pytest
from pybtst2024._core import Money


@pytest.fixture
def money_12():
    return Money(12)


@pytest.fixture
def money_14():
    return Money(14)


def test_equals(money_12, money_14):
    equal_money = Money(12)
    assert money_12 == money_12
    assert money_12 == equal_money
    assert not money_12 == money_14


def test_add(money_12, money_14):
    expected = Money(26)
    result = money_12 + money_14
    assert result == expected
