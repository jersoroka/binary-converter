import unittest
from app import conversion_calcs


class TestCalc(unittest.TestCase):

    def test_find_exponent(self):
        self.assertEqual(conversion_calcs.find_exponent(1), 0)
        self.assertEqual(conversion_calcs.find_exponent(4), 2)
        self.assertEqual(conversion_calcs.find_exponent(16), 4)
        self.assertEqual(conversion_calcs.find_exponent(3), 1)
        self.assertEqual(conversion_calcs.find_exponent(53), 5)

    def test_make_binary(self):
        self.assertEqual(conversion_calcs.make_binary([0, 1, 2, 3, 4, 5]), "111111")
        self.assertEqual(conversion_calcs.make_binary([0, 2, 4]), "10101")
        self.assertEqual(conversion_calcs.make_binary([5]), "100000")

    def test_find_binary(self):
        self.assertEqual(conversion_calcs.find_binary(1), '1')
        self.assertEqual(conversion_calcs.find_binary(4), '100')
        self.assertEqual(conversion_calcs.find_binary(3), '11')
        self.assertEqual(conversion_calcs.find_binary(53), '110101')

    def test_twos_complement(self):
        self.assertEqual(conversion_calcs.twos_complement("1"), "1")
        self.assertEqual(conversion_calcs.twos_complement("1110"), "0010")
        self.assertEqual(conversion_calcs.twos_complement("0001"), "1111")
        self.assertEqual(conversion_calcs.twos_complement("101011"), "010101")

    def test_binary_convert(self):
        self.assertEqual(conversion_calcs.binary_convert(0), 0)
        self.assertEqual(conversion_calcs.binary_convert(-4), 100)
        self.assertEqual(conversion_calcs.binary_convert(-17), 1111)
        self.assertEqual(conversion_calcs.binary_convert(4), 100)
        self.assertEqual(conversion_calcs.binary_convert(17), 10001)


if __name__ == '__main__':
    unittest.main()
