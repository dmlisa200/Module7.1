
import unittest
from fun_with_collections.sort_and_search_array import search_array
#from fun_with_collections.sort_and_search_array import sort_array, my_list

class MyTestCase(unittest.TestCase):
    def test_search_array(self):
        self.assertEqual(search_array(33), 4)
"""
class MyTestClass(unittest.TestCase):
    def test_sort_array(self):
        self.assertEqual(sort_array(my_list), [])
"""

if __name__ == '__main__':
    unittest.main()
