import unittest
from handling_operator import HandlingOperator


class TestHandlingOperator(unittest.TestCase):
    def test_normal_case(self):
        handling = HandlingOperator()
        pricelists = ['operator_A.txt', 'operator_B.txt']
        dial = '4673212345'
        handling.add_all_pricelists(pricelists)
        handling.dial_number = dial
        self.assertEqual(handling.find_cheapest_operator(), 'operator_B.txt', "Incorrect operator")
        
    def test_none_match(self):
        handling = HandlingOperator()
        pricelists = ['operator_A.txt', 'operator_B.txt']
        dial = '3214567890'
        handling.add_all_pricelists(pricelists)
        handling.dial_number = dial
        self.assertEqual(handling.find_cheapest_operator(), '', "Operator should not exist, so return empty!")


if __name__ == '__main__':
    unittest.main()