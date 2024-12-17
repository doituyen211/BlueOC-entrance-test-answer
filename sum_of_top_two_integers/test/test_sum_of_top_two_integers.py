import unittest
from sum_of_top_two_integers.sum_of_top_two_intergers import find_sum_top_two_integers

class TestSumOfTwoIntegers(unittest.TestCase):
    def test_find_sum_top_two_integers(self):
        """
        This function is designed to find the sum of the top two integers in a list.
        """

        # normal case
        input_array = [1, 4, 5, 3, 5]
        result = find_sum_top_two_integers(input_array)
        self.assertEqual(result, 10)

        # case: have two element in list
        input_array = [10, 20]
        result = find_sum_top_two_integers(input_array)
        self.assertEqual(result, 30)

        # case: with negative number
        input_array = [-1, -5, -3, -2]
        result = find_sum_top_two_integers(input_array)
        self.assertEqual(result, -3)

        with self.assertRaises(ValueError):
            find_sum_top_two_integers([1]) 

if __name__ == "__main__":
    unittest.main()
