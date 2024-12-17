import unittest
from string_length_frequency.string_length_frequency import find_most_frequent_string_lengths

class TestStringLengthFrequency(unittest.TestCase):
    def test_find_most_frequent_string_lengths(self):
        """
        This function is likely designed to find the most frequent string lengths in a given dataset.
        """
        # normal case
        input_strings = ['a', 'ab', 'abc', 'cd', 'def', 'gh']
        result = find_most_frequent_string_lengths(input_strings)
        self.assertEqual(result, ['ab', 'cd', 'gh'])

        # case: different lengths but the same number of occurrences
        input_strings = ['a', 'bb', 'ccc']
        result = find_most_frequent_string_lengths(input_strings)
        self.assertEqual(result, ['a', 'bb', 'ccc'])

        # case: two different lengths with a frequency greater than one time
        input_strings = ['aa', 'abc', 'bb', 'def', 'cc', 'ghi']
        result = find_most_frequent_string_lengths(input_strings)
        self.assertEqual(result, ['aa', 'abc', 'bb', 'def', 'cc', 'ghi'])

        # case: empty array
        input_strings = []
        result = find_most_frequent_string_lengths(input_strings)
        self.assertEqual(result, [])

if __name__ == "__main__":
    unittest.main()
