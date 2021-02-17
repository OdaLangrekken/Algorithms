def binary_search(sorted_list, target_value):
    """Function that performs binary search for target_value in a sorted list.

       Parameters:
           sorted_list (iterable): a sorted list of integers.
           target_value (int): value to search for in sorted_list. 

        Returns:
           target_index (int): index of target variable in sorted_list.
    """
    start_index = 0
    end_index = len(sorted_list) - 1
    while start_index < end_index - 1:
        middle_index = (end_index - start_index) // 2
        middle_val = sorted_list[middle_index]
        if middle_val == target_value:
            return middle_index
        if target_value < middle_val:
            end_index = middle_index
        else:
            start_index = middle_index
    return -1



