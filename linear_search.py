
"""This is a linear search algorithm which execution time is linear.  
It's worst case O(n). 
"""

def linear_search(itemList, searchKey):
    """This function will  return search item index from the list if found it otherwise it will return -1
    """
    for i in range(0, len(itemList)): 
        if itemList[i] == searchKey:
            return i
    return -1

def print_output(index):
    if index != -1:
        print('This item is found in the list and index is: ', index)
    else:
        print('Item isn\'t found here!')

if __name__ == '__main__':
    list = [1,24,35,3,5,3,7,9,34,89,12,98]

    result = linear_search(list, 52)
    print_output(result)

    result1 = linear_search(list, 5)
    print_output(result1)

    result2 = linear_search(list, 16)
    print_output(result2)