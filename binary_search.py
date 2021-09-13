
"""Binary search is a searching algorithm only for sorted list. It's applicable only for sorted list
It's worst case O(logn)
"""

def binary_search(sorted_list, key):
    """This function will return index of that key which is searching if found otherwise it will return -1
    """
    start_index = 0
    end_index = len(sorted_list) -1

    while(start_index <= end_index):
        mid_index = (start_index + end_index) // 2
        if sorted_list[mid_index] == key:
            return mid_index
        elif sorted_list[mid_index] <  key:
            start_index = mid_index + 1
        else:
            end_index = mid_index - 1
    return -1


def print_output(index):
    if index != -1:
        print('This is a output of the binary search: Index of that key: ',index)
    else:
        print('Not found this key in the list!')

if __name__ == "__main__":
    sorted_list = [2,4,6,7,8,9,12,56,123,231,311,412,521,631]

    index = binary_search(sorted_list, 12)
    print_output(index)

    index1 = binary_search(sorted_list, 233)
    print_output(index1)
