import pytest
from pybtst2024._util import _div

def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        _div(1,0)
