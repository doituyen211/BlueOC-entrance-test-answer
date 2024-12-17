def find_sum_top_two_integers(input_array):
    """
    This function is designed to find the sum of the top two integers in a given array.
    
    :param input_array: Great! To find the sum of the top two integers in the input array, you can use
    the following Python code:
    """
    # Check to ensure that the input array has at least two numbers.
    if len(input_array) < 2:
        raise ValueError("Array must have two numbers !")
    
    # Declare the largest and the second largest number.
    largest  = second_largest = float('-inf')
    
    # This part of the code is iterating through each number in the input array and updating the
    # variables `largest` and `second_largest` accordingly.
    for num in input_array:
        if num > largest:
            second_largest = largest
            largest = num
        elif num > second_largest:
            second_largest = num

    # Calculate sum of the two largest numbers.
    sum_result = largest + second_largest
    
    # return the result.
    return sum_result

if __name__ == "__main__":
    inputs = [1, 4, 5, 3, 5]
    result = find_sum_top_two_integers(inputs)
    print(result)
