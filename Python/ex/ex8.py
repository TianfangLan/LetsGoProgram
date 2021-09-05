def edit_distance(s1, s2):
    ''' (str, str) -> int
    the funtcion will return the edit distance of two strings.
    >>> edit_distance('abc', 'bbc')
    1
    '''
    if ((len(s1) == 1 and s1 == s2) or len(s1) == 0):
        result = 0
    elif (len(s1) == 1 and s1 != s2):
        result = 1
    elif (s1[0] == s2[0]):
        result = edit_distance(s1[1:], s2[1:])
    elif (s1[0] != s2[0]):
        result = 1 + edit_distance(s1[1:], s2[1:])
    return result


def subsequence(s1, s2):
    ''' (str, str) -> bool
    the function will return whether the s1 is a subsequence of s1.
    >>> subsequence('dog', 'XJSAdABo123512g')
    True
    '''
    # do the case when either s1 or s2 is an empty string
    if ((len(s1) == 0 and len(s2) == 0) or (len(s1) == 0 and len(s2) != 0)):
        result = True
    elif (len(s1) != 0 and len(s2) == 0):
        result = False
    # do the case when neither of s1 nor s2 is empty
    # when it is the smallest case, and s1 may in s2
    # 1: the s1 is in s2
    elif (len(s1) == 1 and s1 == s2[0]):
        result = True
    # 3: s1 is sure not be in s2, because s2 is running out
    elif (len(s2) == 1 and s1 != s2):
        result = False
    # 2: s1 is not in s2 so far, have to go further in s2
    elif (len(s1) == 1 and s1 != s2[0]):
        result = subsequence(s1, s2[1:])
    # when neither s1 nor s2 is running out
    # when the first character of the s1 is found in s2
    elif (len(s2) >= 2 and s1[0] == s2[0]):
        # both jump to next
        result = subsequence(s1[1:], s2[1:])
    # when the first character of s1 is not found
    elif (len(s2) >= 2 and s1[0] != s2[0]):
        # go further in s2
        result = subsequence(s1, s2[1:])
    return result


def perms(s):
    ''' (str) -> set
    the function will return a set of all possible permutations of the letters
    in s.
    >>> perms('abc')
    {'abc', 'bca', 'cba', 'cab', 'acb', 'bac'}
    '''
    # set a set for returning
    result = set()
    # when input the empty string, should return a empty set
    if (len(s) == 0):
        result.add('')
    # when input a single letter, should return the set with only the letter
    elif (len(s) == 1):
        result.add(s)
    # when the input is a longer string
    elif (len(s) >= 1):
        # small_set is the perm of the after letters
        small_set = perms(s[1:])
        # small_length represent the length of the size of the string s
        length = len(s)
        # turn the set into list
        for string in small_set:
            for position in range(0, length):
                new_string = string[0:position] + s[0] + string[position:]
                result.add(new_string)
    return result
