def rsum(L):
    ''' (list) -> int
    The function will return the sum of all elements in the given list.
    REQ: the input should be a list with Ls
    REQ: Ls is an integer, the empty list, or a list of Ls
    >>> rsum([1, 2, [], [1, 3, []]])
    7
    '''
    # when the input list is an empty list
    if (len(L) == 0):
        result = 0
    # do the smallest case and when it is a int
    elif (len(L) == 1 and isinstance(L[0], int)):
        result = L[0]
    # when it is a empty list, give back 0.
    elif (len(L) == 1 and L[0] == []):
        result = 0
    # when the element is not a int, then get into the list and find the
    # sum of the list, add it.
    elif (len(L) == 1 and isinstance(L[0], list)):
        result = rsum(L[0])
    # when the first elment of the list is an empty list.
    elif (len(L) > 1 and L[0] == []):
        result = 0 + rsum(L[1:])
    # when there is 1+ elements in the list, let the first int add to the sum
    # of the rest
    elif (len(L) > 1 and isinstance(L[0], int)):
        result = L[0] + rsum(L[1:])
    # when the first element in the list is a list, calculate the sum of the
    # list first. then add to the sum of the rest.
    elif (len(L) > 1 and isinstance(L[0], list)):
        result = rsum(L[0]) + rsum(L[1:])
    return result


def rmax(L):
    ''' (list) -> int
    The function will return the max number in the list
    REQ: the input should be a list with Ls
    REQ: Ls is an integer, the empty list, or a list of Ls
    >>> rmax([1, 2, [], [1, 3, []]])
    3
    '''
    # do the smallest case and when it is a int
    if (len(L) == 1 and isinstance(L[0], int)):
        result = L[0]
    # when it is a empty list, give back None.
    elif (len(L) == 1 and L[0] == []):
        result = None
    # when the element is not a int, return the largest int in the list
    elif (len(L) == 1 and isinstance(L[0], list)):
        result = rmax(L[0])
    else:
        # get the max of the new element and the max of the rest of the list
        record = rmax(L[1:])
        # if the first element is an empty list, sign it to None
        if (L[0] == []):
            new = None
        # if the first element is a list, find the max of the list
        elif (isinstance(L[0], list)):
            new = rmax(L[0])
        else:
            new = L[0]
        if (record is None):
            result = new
        elif (new is None):
            result = record
        elif (record >= new):
            result = record
        elif (record < new):
            result = new
    return result


def second_helper(L):
    ''' (list) -> tuple or None
    The helper function will return a tuple contains the smallest and the
    second smallest number in the list. (smallest, second smallest)
    REQ: the input should be a list with Ls
    REQ: L is an integer, the empty list, or a list of Ls
    >>> second_helper([1, 2, [], [1, 3, []]])
    (1,1)
    >>> second_helper([1, 2, [], [-1, 3, []]])
    (-1,1)
    '''
    # do the smallest case and when it is a int
    if (len(L) == 1 and isinstance(L[0], int)):
        result = (L[0], None)
    # when it is a empty list, give back None.
    elif (len(L) == 1 and L[0] == []):
        result = None
    # when the element is not a int, return the tuple with
    elif (len(L) == 1 and isinstance(L[0], list)):
        result = second_helper(L[0])
    else:
        record = second_helper(L[1:])
        if (L[0] == []):
            # if the certain list is empty, sign new to None
            new = None
        # if the certain element is a list, create the tuple
        elif (isinstance(L[0], list)):
            new = second_helper(L[0])
            # if the element is an int.
        else:
            # if the number is an int, store a tuple in the new
            new = (L[0], None)
        # Note: new could be tuple or None
        # Note: record can be tuple or None
        if (new is None and record is None):
            # both new and record have not got the number return None
            result = None
        elif (record is None):
            # there is no int in the rest of the list
            result = new
        elif (new is None):
            # the certain element is an empty list
            result = record
        # position the tuple into the result
        # when both the new and record only contains 1 int
        elif (isinstance(new, tuple) and new[1] is None and
              record[1] is None and new[0] <= record[0]):
            result = (new[0], record[0])
        elif (isinstance(new, tuple) and new[1] is None and
              record[1] is None and new[0] > record[0]):
            result = (record[0], new[0])
        # when new only contains 1 int and record contains 2 ints
        elif (isinstance(new, tuple) and new[1] is None and
              record[1] is not None and record[1] >= new[0] >= record[0]):
            result = (record[0], new[0])
        elif (isinstance(new, tuple) and record[1] is not None and
              new[0] >= record[1]):
            result = record
        elif (isinstance(new, tuple) and new[1] is None and
              record[1] is not None and new[0] <= record[0]):
            result = (new[0], record[0])
        # when new contains 2 ints and record contains 1 int
        elif (isinstance(new, tuple) and new[1] is not None and
              record[1] is None and new[1] >= record[0] >= new[0]):
            result = (new[0], record[0])
        elif (isinstance(new, tuple) and new[1] is not None and
              record[0] >= new[1]):
            result = new
        elif (isinstance(new, tuple) and new[1] is not None and
              record[1] is None and record[0] < new[0]):
            result = (record[0], new[0])
        # when both new and record contain 2 ints
        # when result is the combination of new and record
        elif (isinstance(new, tuple) and record[0] <= new[0] <= record[1]):
            result = (record[0], new[0])
        elif (isinstance(new, tuple) and new[0] <= record[0] <= new[1]):
            result = (new[0], record[0])
    return result


def second_smallest(L):
    ''' (list) -> int
    The function will return the second smallest int in the list.
    REQ: the input should be a list with Ls
    REQ: L is an integer, the empty list, or a list of Ls
    >>> second_helper([1, 2, [], [1, 3, []]])
    1
    >>> second_helper([1, 2, [], [-1, 3, []]])
    1
    '''
    return second_helper(L)[1]


def sum_helper(L):
    ''' (list) -> tuple
    The function will return the smallest and the biggest int in the list in
    the form of tuple.(smallest, largest)
    REQ: the input should be a list with Ls
    REQ: L is an integer, the empty list, or a list of Ls
    >>> sum_helper([1, 2, [], [1, 3, []]])
    (1,3)
    >>> sum_helper([1, 2, [], [-1, 3, []]])
    (-1,3)
    '''
    # do the smallest case and when it is a int
    if (len(L) == 1 and isinstance(L[0], int)):
        result = (L[0], L[0])
    # when it is a empty list, give back None.
    elif (len(L) == 1 and L[0] == []):
        result = None
    # when the element is not a int, return the tuple with function
    elif (len(L) == 1 and isinstance(L[0], list)):
        result = sum_helper(L[0])
    else:
        record = sum_helper(L[1:])
        if (L[0] == []):
            # if the certain list is empty, sign new to None
            new = None
        # if the certain element is a list, create the tuple
        elif (isinstance(L[0], list)):
            new = sum_helper(L[0])
            # if the element is an int.
        else:
            # if the number is an int, store a tuple in the new
            new = (L[0], L[0])
        # position the tuple into result
        # Note: new and result both can only a list with 2 ints or None
        # when there is at lease one of new and record is None
        if (new is None and record is None):
            result = None
        elif (new is None):
            result = record
        elif (record is None):
            result = new
        # when new has the smallest and record has the largest
        elif (new[0] <= record[0] and new[1] <= record[1]):
            result = (new[0], record[1])
        # when new has both the smallest and largest
        elif (new[0] <= record[0] and new[1] >= record[1]):
            result = new
        # when record has the smallest and the largest
        elif (new[0] >= record[0] and new[1] <= record[1]):
            result = record
        # when record has the smallest and new has the largest
        elif (new[0] >= record[0] and new[1] >= record[1]):
            result = (record[0], new[1])
    return result


def sum_max_min(L):
    ''' (list) -> int
    The function will return the sum of the largest and smallest number in the
    list.
    REQ: the input should be a list with Ls
    REQ: L is an integer, the empty list, or a list of Ls
    >>> sum_max_min([1, 2, [], [1, 3, []]])
    4
    >>> sum_max_min([1, 2, [], [-1, 3, []]])
    2
    '''
    record = sum_helper(L)
    return record[0] + record[1]
