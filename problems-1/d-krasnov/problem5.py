import math
import unittest


def factorize_number(num):
    factors = []
    divisor = 2

    upper_bound = math.sqrt(num)

    while divisor <= upper_bound:
        if num % divisor == 0:
            count = 0
            while num % divisor == 0:
                num //= divisor
                count += 1
            factors.append([divisor, count])
        divisor += 1

    if num > 1:
        factors.append([num, 1])
    return factors


class TestFactorizeNumber(unittest.TestCase):
    def test_prime_number(self):
        self.assertEqual([[7, 1]], factorize_number(7))

    def test_multiple_prime_factors(self):
        self.assertEqual([[2, 2], [5, 1]], factorize_number(20))

    def test_repeated_prime_factors(self):
        self.assertEqual([[2, 3], [3, 2]], factorize_number(72))

    def test_large_number(self):
        self.assertEqual([[3, 4], [37, 1], [333667, 1]], factorize_number(999999999))

    def test_zero(self):
        self.assertEqual([],factorize_number(0))


if __name__ == '__main__':
    unittest.main()
