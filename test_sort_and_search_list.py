import unittest
from fun_with_collections.sort_and_search_list import search_list
from fun_with_collections.sort_and_search_list import sort_list, my_list

class MyTestCase(unittest.TestCase):
    def test_search_list(self):
        self.assertEqual(search_list(33), 4)

class MyTestClass(unittest.TestCase):
    def test_sort_list(self):
        self.assertEqual(sort_list(my_list), [])


if __name__ == '__main__':
    unittest.main()
