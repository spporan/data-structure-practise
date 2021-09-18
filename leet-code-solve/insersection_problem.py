
def intersection(nums1, nums2):

    if len(nums1) < len(nums2):
        return intersection(nums2, nums1)
    dicts = {}
    for item in nums1:
        dicts[item] = dicts.get(item,0) + 1
    res = []
    for j in nums2:
        if dicts.get(j,0) > 0:
            dicts[j] = dicts.get(j) - 1
            res.append(j)
    return res

if __name__ == "__main__":
    list = intersection([1,4,4,23,4,6,8], [4, 5,4, 6, 7,8])
    print(list)
