def find_index_of_max_value(array):
    """
    This function finds the indices of the maximum value in a given array.
    
    :param array: An array of numbers
    """

    max_index_arr = [] # declare array need to find.
    max_value = array[0] # Assume that max value is the first element.
    
    # This part of the code is iterating over the elements of the input array to find the indices of
    # the maximum value(s) in the array. Here's a breakdown of what it does:
    for i in range(len(array)):
        if array[i] > max_value:
            max_value = array[i]
            max_index_arr.clear()
            max_index_arr.append(i)
        elif array[i] == max_value:
            max_index_arr.append(i)

    # return the array contains the index of the largest values.
    return max_index_arr 


def find_most_frequent_string_lengths(inputs) :
    """
    This function aims to find the most frequent string lengths in a given list of strings.
    
    :param inputs: A list of strings for which you want to find the most frequent string lengths
    """
    if len(inputs) != 0:
    
        # Create a list of lengths of each string.
        string_lengths = []
        for i in inputs:
            string_lengths.append(len(i))

        # Create a unique list of each element.
        unique_element = list(set(string_lengths))

        # Count the frequency of occurrence of each length.
        length_frequencies = []
        for i in unique_element:
            value = string_lengths.count(i)
            length_frequencies.append(value)

        # Find the index of the lengths with the highest frequency.
        max_frequency_indices = find_index_of_max_value(length_frequencies)

        # Find the index of the length with the highest frequency.
        index_length_frequencies = []
        for i, num in enumerate(string_lengths):
            for j in max_frequency_indices:
                if num == unique_element[j]:
                    index_length_frequencies.append(i)

        # Get the strings whose length corresponds to the highest frequency.
        result_strings = []
        for i in index_length_frequencies:
            result_strings.append(inputs[i])
            
        #return the result strings.
        return result_strings
    else:
        return inputs
        
        


if __name__ == "__main__":
    inputt = ['a', 'ab', 'abc', 'cd', 'def', 'gh']
    result = find_most_frequent_string_lengths(inputt)
    print("Strings with the most frequent lengths: ", result)

