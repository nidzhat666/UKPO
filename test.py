import unittest
from main import calc


class TestWhite(unittest.TestCase):
    def test_normal(self):
        res = calc('2+(-5)*(7-8)')
        self.assertEqual(res, 7)

    def test_str(self):
        res = calc('1+a+c+d')
        self.assertEqual(res, 'Не верный формат')


if __name__ == '__main__':
    # coverage report -m
    unittest.main()