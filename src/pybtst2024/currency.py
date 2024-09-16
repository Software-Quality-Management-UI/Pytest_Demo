from pybtst2024._core import Money


class Currency:
    def __init__(self, amount: int, currency_code: str):
        self.money = Money(amount)
        self.currency_code = currency_code.upper()

    def get_amount(self):
        return self.money.getAmount()

    def get_currency(self):
        return self.currency_code

    def __add__(self, other):
        if self.currency_code != other.currency_code:
            raise ValueError(
                f"Cannot add amounts in different currencies: {self.currency_code} and {other.currency_code}"
            )
        result_money = self.money + other.money
        return Currency(result_money.getAmount(), self.currency_code)

    def convert_to(self, target_currency_code, exchange_rate):
        """
        Converts this currency to the target currency using a fixed exchange rate.

        :param target_currency_code: str, the target currency code
        :param exchange_rate: float, the rate to convert from current currency to target currency
        :return: Currency object in the target currency
        """
        if exchange_rate <= 0:
            raise ValueError("Exchange rate must be positive.")
        converted_amount = int(self.money.getAmount() * exchange_rate)
        return Currency(converted_amount, target_currency_code.upper())

    def __eq__(self, other):
        return self.money == other.money and self.currency_code == other.currency_code

    def __repr__(self):
        return f"{self.money.getAmount()} {self.currency_code}"
