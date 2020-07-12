import unittest

from main import MyHashTable


class MyTestCase(unittest.TestCase):
    def test_init(self):
        my_hash_table = MyHashTable()
        self.assertEqual(len(my_hash_table.data), 1024)

    def test_set(self):
        my_hash_table = MyHashTable()
        my_hash_table.set('a', 1)
        self.assertEqual(my_hash_table.data[my_hash_table.get_hash('a')], 1)

    def test_get(self):
        my_hash_table = MyHashTable()
        my_hash_table.set('a', 1)

        self.assertEqual(my_hash_table.get('a'), 1)


if __name__ == '__main__':
    unittest.main()
