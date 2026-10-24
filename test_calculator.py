import pytest
from calculator import Calculator


@pytest.fixture
def calc():
    return Calculator()


def test_add(calc):
    assert calc.add(2.0, 3.0) == 5.0
    assert calc.add(-1.0, 1.0) == 0.0


def test_subtract(calc):
    assert calc.subtract(5.0, 3.0) == 2.0
    assert calc.subtract(1.0, 5.0) == -4.0


def test_multiply(calc):
    assert calc.multiply(3.0, 3.0) == 9.0
    assert calc.multiply(-2.0, 4.0) == -8.0


def test_divide(calc):
    assert calc.divide(10.0, 2.0) == 5.0


def test_divide_by_zero(calc):
    # Тест ожидает ошибку ValueError при делении на ноль
    with pytest.raises(ValueError):
        calc.divide(5.0, 0.0)


# --- Новые тесты с параметризацией ---

@pytest.mark.parametrize(
    "a, b, expected",
    [
        (7.5, 2.5, 3.0),                    # обычные дробные
        (-9.0, 3.0, -3.0),                  # отрицательное делимое
        (1.0, 3.0, pytest.approx(1 / 3)),   # периодическая дробь
        (0.0, 5.0, 0.0),                    # ноль в числителе
    ],
)
def test_divide_parametrized(calc, a, b, expected):
    assert calc.divide(a, b) == expected


@pytest.mark.parametrize(
    "a, b, expected",
    [
        (10.5, -5.5, 5.0),
        (-1.0, -1.0, -2.0),
        (0.1, 0.2, pytest.approx(0.3)),     # проблема точности float
    ],
)
def test_add_parametrized(calc, a, b, expected):
    assert calc.add(a, b) == expected
