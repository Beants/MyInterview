import unittest

from main import MyStack


class MyTestCase(unittest.TestCase):
    def test_l_push(self):
        my_stuck = MyStack()
        my_stuck.l_push(1)
        self.assertEqual(my_stuck.data, [1])

    def test_r_push(self):
        my_stuck = MyStack()
        my_stuck.r_push(1)
        self.assertEqual(my_stuck.data, [1])

    def test_l_pop(self):
        my_stuck = MyStack()
        my_stuck.data = [1]
        my_stuck.l_pop()
        self.assertEqual(my_stuck.data, [])

    def test_r_pop(self):
        my_stuck = MyStack()
        my_stuck.data = [1]
        my_stuck.r_pop()
        self.assertEqual(my_stuck.data, [])


if __name__ == '__main__':
    unittest.main()
