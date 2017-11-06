import calculator

def test_divide_called_returnes_quotient():
    dividend = 1
    divisor = 2
    expected_quotient = .5

    actual_quotient = calculator.divide(
        dividend,
        divisor
)

    assert actual_quotient == expected_quotient
