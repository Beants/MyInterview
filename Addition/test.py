import unittest

from Addition.main import Addition


class MyTestCase(unittest.TestCase):
    def test_addition(self):
        self.assertEqual(Addition.addition('1111211111111111111111111111111111111111111119', '111'), '1111211111111111111111111111111111111111111230')


if __name__ == '__main__':
    unittest.main()
