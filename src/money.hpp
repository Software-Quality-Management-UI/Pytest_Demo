#pragma once
#include <string>

namespace pybtst {

class Money {
private:
  double amount;

public:
  Money(double amount) : amount(amount) {}

  double getAmount() const { return amount; }

  Money operator+(const Money &m) const { return Money(amount + m.getAmount()); }

  bool operator=(const Money &m) const { return amount == m.getAmount(); }

  std::string toString() const { return std::to_string(amount); }
};

} // namespace pybtst
