import pytest
import numpy as np

from pybtst2024._core import Money


@pytest.fixture
def money_12():
    return Money(12)


@pytest.fixture
def money_14():
    return Money(14)


@pytest.fixture
def money_values():
    # Create an array of Money objects using numpy
    amounts = np.array([12, 14, 15, 20])
    money_array = np.array([Money(amount) for amount in amounts])
    return money_array


def test_equals(money_12, money_14):
    equal_money = Money(12)
    assert money_12 == money_12
    assert money_12 == equal_money
    assert not money_12 == money_14


def test_add(money_12, money_14):
    expected = Money(26)
    result = money_12 + money_14
    assert result == expected


def test_add_with_numpy(money_values):
    adder = Money(10)

    result_array = np.array([money + adder for money in money_values])

    expected_amounts = np.array([22, 24, 25, 30])

    result_amounts = np.array([money.getAmount() for money in result_array])

    np.testing.assert_array_equal(result_amounts, expected_amounts)


def test_equality_with_numpy(money_values):
    equal_money = Money(12)
    results = np.array([money == equal_money for money in money_values])

    expected_results = np.array([True, False, False, False])

    np.testing.assert_array_equal(results, expected_results)


def test_large_scale_addition():
    np.random.seed(1995)
    random_amounts = np.random.randint(1, 100, size=1000)
    money_array = np.array([Money(amount) for amount in random_amounts])

    adder = Money(5)
    result_array = money_array + adder

    expected_amounts = random_amounts + 5
    result_amounts = np.array([money.getAmount() for money in result_array])

    np.testing.assert_array_equal(result_amounts, expected_amounts)
