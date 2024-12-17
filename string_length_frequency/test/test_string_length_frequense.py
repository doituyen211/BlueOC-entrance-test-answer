import unittest
from string_length_frequency.string_length_frequency import find_most_frequent_string_lengths

class TestStringLengthFrequency(unittest.TestCase):
    def test_find_most_frequent_string_lengths(self):
        """
        This function is likely designed to find the most frequent string lengths in a given dataset.
        """

        input_strings = ['a', 'ab', 'abc', 'cd', 'def', 'gh']
        result = find_most_frequent_string_lengths(input_strings)
        self.assertEqual(result, ['ab', 'cd', 'gh'])
        
        input_strings = ['a', 'bb', 'ccc']
        result = find_most_frequent_string_lengths(input_strings)
        self.assertEqual(result, ['a', 'bb', 'ccc'])

        input_strings = ['abc', 'def', 'ghi']
        result = find_most_frequent_string_lengths(input_strings)
        self.assertEqual(result, ['abc', 'def', 'ghi'])

        input_strings = []
        result = find_most_frequent_string_lengths(input_strings)
        self.assertEqual(result, [])

if __name__ == "__main__":
    unittest.main()
