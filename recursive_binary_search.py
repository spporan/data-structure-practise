
"""This is also a binary search implementation using recursive way."""

def recursive_binary_search(list, search_key):
    if len(list) == 0:
        return False
    else:
        midpoint = len(list)//2
        
        if list[midpoint] == search_key:
            return True
        else:
            if list[midpoint] > search_key:
                return recursive_binary_search(list[:midpoint], search_key)

            elif list[midpoint] < search_key:
                return recursive_binary_search(list[midpoint+1:],search_key)
            else:
                return False

"""This is a output function for the binary search"""

def outPut_print(is_found):
    if is_found:
        print("Search item is found!")
    else:
        print("Search item isn't found!")

if __name__ == "__main__":
    sorted_list = [2,4,6,7,8,9,12,56,123,231,311,412,521,631]

    index = recursive_binary_search(sorted_list, 12)
    outPut_print(index)

    index1 = recursive_binary_search(sorted_list, 233)
    outPut_print(index1)
