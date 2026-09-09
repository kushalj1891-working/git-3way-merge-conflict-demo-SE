```python
from calculator import Calculator


def test_addition():
    calculator = Calculator()
    assert calculator.add(10, 5) == 15


def test_subtraction():
    calculator = Calculator()
    assert calculator.subtract(10, 5) == 5


def test_multiplication():
    calculator = Calculator()
    assert calculator.multiply(10, 5) == 50


def test_division():
    calculator = Calculator()
    assert calculator.divide(10, 5) == 2
```
