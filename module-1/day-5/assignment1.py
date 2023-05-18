def mergeTwoLists(list1, list2):
    result = list1 + list2
    for i in range(len(result)-1):
        for j in range(i, len(result)):
            if result[i] > result[j]:
                result[i], result[j] = result[j], result[i]    
    return result

if __name__ == '__main__':
    assert mergeTwoLists([1, 3, 6], [5, 7, 8, 9]) == [1, 3, 5, 6, 7, 8, 9]
    assert mergeTwoLists([1, 2, 3], [4, 5]) == [1, 2, 3, 4, 5]
    assert mergeTwoLists([4, 5], [1, 2, 3]) == [1, 2, 3, 4, 5]
    assert mergeTwoLists([2, 2, 2], [2, 2, 2]) == [2, 2, 2, 2, 2, 2]
    assert mergeTwoLists([1, 2, 3], []) == [1, 2, 3]
    assert mergeTwoLists([], [1, 2, 3]) == [1, 2, 3]