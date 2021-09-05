def greeting(name):
    ''' the function will take a person's name and return:
    'Hello <name> how are you today?'
    REQ: the input should be a string
    >>> greeting('Lan')
    'Hello Lan how are you today?'
    >>> greeting('Nick')
    'Hello Nick how are you today?'
    '''
    # create the returning str
    result = "Hello "
    result += name
    result += ' how are you today?'
    # return the result
    return result


def mutate_list(in_list):
    ''' the function will take a list as a parameter, if the element
    is integer, it will be multipled by 2. If it is boolean, it will be
    inverted. If it is a string, its first and last characters will be removed.
    The 0th element must be set to the string Hello.
    REQ: the list must contains at least 1 element in it
    REQ: the string element should contains at least 2 characters in it
    >>> mutate_list([3, 4, 'bb', False])
    None
    '''
    # get the length of the list
    length = len(in_list)
    # for the 0th element it should be mutated to 'Hello'
    in_list[0] = 'Hello'
    if (length >= 2):
        # for the rest of the elements, use loop to swap them
        for i in range(1, length):
            # if element is an integer
            if (type(in_list[i]) == int):
                # double the integer
                in_list[i] = in_list[i] * 2
            # if the element is a bool
            elif (type(in_list[i]) == bool):
                # bool is inverted
                in_list[i] = not in_list[i]
            # if the element is a string
            elif (type(in_list[i]) == str):
                # the first and last characters will be removed.
                # set the length of the str
                # if the string contains more than 2 characters
                len_str = len(in_list[i])
                in_list[i] = str(in_list[i][1: (len_str - 1)])


def merge_dicts(dict1, dict2):
    ''' the fuction will take two dictionaries and returns a new dictionary
    with all keys. If teh dictionaries has the same key then append the value
    in the dict2 to the value in the dict1
    REQ: dict1 and dict2 should be in the format of {str: list of ints}
    >>> d1 = {'a': [1, 2, 3], 'b': [4], 'c': [5, 6, 7]}
    >>> d2 = {'a': [2], 'b': [8, 9, 0], 'd': [10, 11, 12]}
    >>> merge_dicts(d1, d2)
    {'a': [1, 2, 3, 2], 'b': [4, 8, 9, 0], 'c': [5, 6, 7], 'd': [10, 11, 12]}
    >>> merge_dicts(d2, d1)
    {'a': [2, 1, 2, 3], 'b': [8, 9, 0, 4], 'c': [5, 6, 7], 'd': [10, 11, 12]}
    '''
    # create a new dictionary for returning
    result = {}
    # copy dict1 and dict2
    dict3 = dict1.copy()
    dict4 = dict2.copy()
    # loop the keys in the dict3(dict1)
    for key1 in dict3:
        # if the current key is not in dict4
        if key1 not in dict4:
            # add the list to the result
            result[key1] = dict3[key1]
        # loop the keys in the dict4(dict2)
        for key2 in dict4:
            # if the current key equals to the key in dict3
            if key1 == key2:
                # add up 2 lists
                result[key1] = dict3[key1] + dict4[key1]
            # if the current key is not exist in dict1 then add it to the
            # the new dictionary
            elif key2 not in dict3:
                result[key2] = dict4[key2]
    return result
