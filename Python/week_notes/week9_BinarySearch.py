def binary_search(data, low, high, target):
    '''(list, int, int, int) -> bool
    return true if target is in the list
    REQ: low & high >=0
    '''
    # The first base case where target can't be found
    if (high < low): 
        result = False
    else:
        mid = (low + high)//2
        # the second base case, where you find the target
        if (data[mid] == target):
            result = True
        elif (target < data[mid]):
            result = binary_search(data, low, mid-1, target)
        else:
            result = binary_search(data, mid+1, high, target)
    return result

def find_index(data, low, high, target):
    '''(list, int, int) -> int
    returns the index of the target in data, if data contains the target. 
    Otherwise returns -1 
    This function uses binary search method of searching
    REQ: low & high >=0
    REQ: data is an ascendingly sorted list 
    '''
    # base case, if high passes low, means target is not in data
    if (high < low): 
        result = -1
    else:
        mid = (low + high)//2
        if (data[mid] == target):
            result = mid
        elif (target < data[mid]):
            result = find_index(data, low, mid-1, target)
        else:
            result = find_index(data, mid+1, high, target)
    return result

if (__name__ == "__main__"):
    data = [1,2,3, 6, 7, 8, 9, 13, 15, 18]
    print(binary_search(data, 0, len(data)-1, 1))
    print(binary_search(data, 0, len(data)-1, 18))
    print(binary_search(data, 0, len(data)-1, 8))
    print(binary_search(data, 0, len(data)-1 , 4))
    print(binary_search(data, 0, len(data)-1, 16))
        
    print(find_index(data, 0, len(data)-1, 1))
    print(find_index(data, 0, len(data)-1, 18))
    print(find_index(data, 0, len(data)-1, 8))
    print(find_index(data, 0, len(data)-1 , 4))
    print(find_index(data, 0, len(data)-1, 16))
    