import unittest
from service import *
from db import select_query

class Test(unittest.TestCase):
    def test_create_order(self):
        expected_result = [(1, 'Akash Sharma', '2023-02-01', 'Coffee', 2, 3.5, 7), (2, 'Nick Jones', '2023-02-02', 'Tea', 1, 2.5, 2.5), (3, 'Alan Sugar', '2023-02-03', 'Coffee', 1, 3.5, 3.5), (4, 'Jim Gates', '2023-02-03', 'Tea', 2, 2.5, 5), (5, 'Amanda Jonny', '2023-02-04', 'Sandwich', 2, 5, 10), (6, 'Ewelina Jones', '2023-02-04', 'Coffee', 2, 3.5, 7), (7, 'David Smith', '2023-02-04', 'Sandwich', 5, 5, 25), (8, 'Vidya Sharma', '2023-02-09', 'Coffee', 2, 3.5, 7)]
        call_function = create_order()
        self.assertEqual(expected_result, call_function)

    def test_read_by_id(self):
        expected_result = [(1, 'Akash Sharma', '2023-02-01', 'Coffee', 2, 3.5, 7)]
        call_function = read_by_id()
        self.assertEqual(expected_result, call_function)

    def test_read_all_qa_cafe_order(self):
        expected_result = [(1, 'Akash Sharma', '2023-02-01', 'Coffee', 2, 3.5, 7), (2, 'Nick Jones', '2023-02-02', 'Tea', 1, 2.5, 2.5), (3, 'Alan Sugar', '2023-02-03', 'Coffee', 1, 3.5, 3.5), (4, 'Jim Gates', '2023-02-03', 'Tea', 2, 2.5, 5), (5, 'Amanda Jonny', '2023-02-04', 'Sandwich', 2, 5, 10), (6, 'Ewelina Jones', '2023-02-04', 'Coffee', 2, 3.5, 7), (7, 'David Smith', '2023-02-04', 'Sandwich', 5, 5, 25)]
        call_function = read_all_qa_cafe_order()
        self.assertEqual(expected_result, call_function)

    def test_update_order_id(self):
        expected_result = [(1, 'Akash Sharma', '2023-02-01', 'Coffee', 2, 3.5, 7)]
        call_function = read_by_id()
        self.assertEqual(expected_result, call_function)

    def test_delete_order_id(self):
        expected_result = [(1, 'Akash Sharma', '2023-02-01', 'Coffee', 2, 3.5, 7)]
        call_function = read_by_id()
        self.assertEqual(expected_result, call_function)

    # def test_delete_all_order_id(self):
    #     expected_result =
    #     call_function = read_by_id()
    #     self.assertEqual(expected_result, call_function)



if __name__ == '__main__':
    unittest.main()
