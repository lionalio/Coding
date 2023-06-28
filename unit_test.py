import unittest
from handling_operator import HandlingOperator


class TestHandlingOperator(unittest.TestCase):
    '''
    Operator A and B file should contain normal prefix with numbers only
    Operator C is a little bit exotic, with some minus and parentheses as separators (for easy reading)
    '''
    def test_normal_case(self):
        print('\n=== Running a very normal test case using two operator ===')
        handling = HandlingOperator()
        pricelists = ['operator_A.txt', 'operator_B.txt']
        dial = '4673212345'
        handling.add_all_pricelists(pricelists)
        handling.dial_number = dial
        self.assertEqual(handling.find_cheapest_operator(), ['operator_B.txt'], "Incorrect operator")
        
    def test_none_match(self):
        print('\n=== Running test case without any pricelist exist ===')
        handling = HandlingOperator()
        pricelists = ['operator_A.txt', 'operator_B.txt']
        dial = '3214567890'
        handling.add_all_pricelists(pricelists)
        handling.dial_number = dial
        self.assertEqual(handling.find_cheapest_operator(), [], "Operator should not exist, so return empty!")

    def test_multiple_min_price(self):
        print('\n=== Running test case with more than one operator has minimum prices ===')
        handling = HandlingOperator()
        pricelists = ['operator_A.txt', 'operator_B.txt', 'operator_C.txt']
        dial = '4673212345'
        handling.add_all_pricelists(pricelists)
        handling.dial_number = dial
        self.assertEqual(handling.find_cheapest_operator(), ['operator_B.txt', 'operator_C.txt'], "Incorrect list of operator")


if __name__ == '__main__':
    unittest.main()