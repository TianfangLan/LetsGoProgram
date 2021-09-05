def rsum(list1):
    ''' (list) -> list
    The function will return the sum of all elements in the given list.
    REQ: the input list should be all int, and at least contains 1 int
    >>> rsum([1, 2, 3])
    6
    >>> rsum([2, 2, 2])
    4
    '''
    if (len(list1) == 1):
        result = list1[0]
    else:
        result = list1[0] + rsum(list1[1:])
    return result


def rmax(list1):
    ''' (list) -> int
    The function will return the biggest number in the list
    REQ: the input list should all be int, and at least contains 1 int
    >>> rmax([1, 2, 3])
    3
    >>> rmax([1, 2, 1])
    2
    '''
    if (len(list1) == 1 or (len(list1) > 1 and (list1[0] >= rmax(list1[1:])))):
        result = list1[0]
    else:
        result = rmax(list1[1:])
    return result


def second_smallest(list1):
    ''' (list) -> int
    The function will return the second small number in the list
    REQ: the input list should all be int, and at least contains 2 ints
    >>> second_smallest([1, 2, 3])
    2
    >>> second_smallest([1, 2, 3, 5, 6])
    2
    '''
    return second_helper(list1)[1]


def second_helper(list1):
    ''' (list) -> tuple
    This helper function will return a tuple of 2 ints contains (smallest int,
    second smallest int).
    REQ: the input list should all be int, and at least contains 2 ints
    >>> second_helper([1, 2, 3])
    (1, 2)
    '''
    # when the list is the smallest size.
    # create the tuple
    if (len(list1) == 2 and list1[0] >= list1[1]):
        result = (list1[1], list1[0])
    elif (len(list1) == 2 and list1[0] < list1[1]):
        result = (list1[0], list1[1])
    # when the list is in bigger size
    else:
        # run the function and store data.
        pre_result = second_helper(list1[1:])
        # make no change when the current is larger than the second smallest
        if (list1[0] >= pre_result[1]):
            result = pre_result
        # when current is in between 2 numbers, change the second smallest
        elif (pre_result[0] <= list1[0] and
              list1[0] <= pre_result[1]):
            result = (pre_result[0], list1[0])
        # when current is smaller than the smallest, change the current to
        # smallest and change the pre_smallest to second smallest.
        elif (list1[0] <= pre_result[0]):
            result = (list1[0], pre_result[0])
    return result


def sum_max_min(list1):
    '''(list) -> int
    The function will return the sum of the max and min number in the list.
    REQ: the input list should all be int, and at least contains 1 int
    >>> sum_max_min([1, 2, 3])
    4
    >>> sum_max_min([0, 2, 3])
    3
    '''
    # store the tuple, not let the helper run 2 times
    result = sum_helper(list1)
    return result[0] + result[1]


def sum_helper(list1):
    ''' (list) -> tuple
    This helper function will return a tuple of 2 ints contains (largest int,
    smallest int).
    REQ: the input list should all be int, and at least contains 1 int
    >>> sum_helper([1, 2, 3])
    (3, 1)
    '''
    # smallest case, when only one int in the list, it is the largest
    # and smallest
    if (len(list1) == 1):
        result = (list1[0], list1[0])
    # the certain element is larger than the largest number in current list
    else:
        # run the function once and store the data
        pre_result = sum_helper(list1[1:])
        if (list1[0] >= pre_result[0]):
            # change the largest number to the certain number
            result = (list1[0], pre_result[1])
            # the certain element is smaller than the smallest number
            # in current list
        elif (list1[0] <= pre_result[1]):
            # change the smallest number to the certain number
            result = (pre_result[0], list1[0])
            # the number is in between the largest and smallest
        else:
            # result should not be changed
            result = pre_result
    return result
