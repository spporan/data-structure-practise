
def merge_sort(list):
    """
    Sorts a list into the assending order
    Retruns a new sorted list

    Divide : Find the midpoint of the list and divide into the sublists
    Conquer: Recursivelly sorts the sublist created as i mentioned before.
    Combine: marge the sorted sublists that created previous steps.

    Overall sorting take time O(nlogn)
    """
    if len(list) <= 1 :
        return []
    
    left_half, right_half = split(list)
    left = merge_sort(left_half)
    right = merge_sort(right_half)

    return merge(left,right)

def split(list):
    """
    Divide a list into two sublist at midpoint and retrun two sublists
    Takes overall O(logn) time
    """
    midpoint = len(list) // 2
    left = list[:midpoint]
    right = list[midpoint:]

    return left, right


def merge(left, right):
    """
    Merge two sublist into a list and sorting them in the proccess and 
    returns a new sorted list
    Runs in overall o(n) times.
    """

    i = 0
    j = 0
    new_list = []

    while i < len(left) and j < len(right):
        if left[i] < right[j] :
            new_list.append(left[i])
            i += 1
        else:
            new_list.append(right[j])
            j += 1
    while i < len(left) :
        new_list.append(left[i])
        i += 1

    while j < len(right):
        new_list.append(right[j])
        j += 1
    
    return new_list

def verify_sort(list):

    if len(list) == 0 or len(list) == 1:
        return True

    return list[0] < list[1] and verify_sort(list[1:])


if __name__ == "__main__":
    alist = [23,5,4,67,0,43,1,8,57,0,8,12,32]
    sorted_list = merge_sort(alist)
    print('Verify ',verify_sort(alist))
    print("verify ", verify_sort(sorted_list))