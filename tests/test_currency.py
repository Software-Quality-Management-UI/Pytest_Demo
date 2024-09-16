import pytest
from pybtst2024.currency import Currency


def test_currency_addition():
    usd1 = Currency(100, "USD")
    usd2 = Currency(50, "USD")
    result = usd1 + usd2

    assert result == Currency(150, "USD")


def test_currency_addition_different_currencies():
    usd = Currency(100, "USD")
    eur = Currency(100, "EUR")

    with pytest.raises(ValueError, match="Cannot add amounts in different currencies"):
        usd + eur


def test_currency_conversion():
    usd = Currency(100, "USD")
    # Assume 1 USD = 0.85 EUR
    eur = usd.convert_to("EUR", 0.85)

    assert eur == Currency(85, "EUR")


def test_invalid_exchange_rate():
    usd = Currency(100, "USD")

    with pytest.raises(ValueError, match="Exchange rate must be positive"):
        usd.convert_to("EUR", 0)  # Invalid exchange rate


def test_repr():
    currency = Currency(100, "usd")
    assert repr(currency) == "100.0 USD"
