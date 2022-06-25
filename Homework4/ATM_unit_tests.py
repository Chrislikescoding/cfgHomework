from unittest import TestCase, main # for all examples

from ATM_code import get_file_content
from ATM_simulation_for_testing import get_pin, check_less_than_balance_values, check_multiple_of_ten, \
    BlankInputError, get_bal


class TestCheckPinFunction(TestCase):
#1 pin should be an int
    def test_is_valid_pin(self):
        expected = int
        returned = type(get_pin())
        self.assertEqual(expected, returned)

#2 withdrawal amount should be less than balance
    def test_withdrawal_lt_balance(self):
         expected = True
         result = check_less_than_balance_values(80)
         self.assertEqual(expected, result)

#3 withdrawal amount should be a multiple of ten
    def test_amount_between_parms(self):
        expected = False
        result = check_multiple_of_ten(25)
        self.assertEqual(expected, result)

#4  def test_bal_is_not_0(self):
        expected = True
        returned = get_bal(10)
        self.assertEqual(expected, returned)

 #5   def test_pin_is_blank(self):
        self.assertRaises((BlankInputError,ValueError,TypeError),get_pin())




if __name__ == '__main__':
    main()
