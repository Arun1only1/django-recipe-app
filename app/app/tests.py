from django.test import SimpleTestCase

from app import calc


class CalcTests(SimpleTestCase):

    def test_add_numbers(self):
        res = calc.sum(5, 10)
        self.assertEqual(res, 15)

    def test_subtract_numbers(self):
        res = calc.subtract(25, 15)
        self.assertEqual(res, 10)
        """ Test that values are subtracted and returned """
