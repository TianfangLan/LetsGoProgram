from container import *


def banana_verify(source, goal, container, moves):
    '''(str, str, Container, list of str) -> bool
    the function will return whether the move method can turn the source string
    into goal string or not.
    REQ: the moves should only contains characters: 'P', 'M', 'G'.
    >>> banana_verify('CAT', 'ACT', Bucket(), ['P', 'M', 'G', 'M'])
    True
    '''
    # set the final bool to be returned
    boolean = False
    # set a result
    result = ''
    # set the length of the list
    len_list = len(moves)
    # set the time of moves
    times = 0
    # set the length of the source
    len_source = len(source)
    for method in moves:
        if method == 'G' or method == 'M':
            times += 1
    for method in moves:
        if (method is 'P' and source != ''):
            # define the current character
            curr = source[0]
            # delete the first character in source
            source = source[1:]
            # try put the current char into container
            try:
                container.put(curr)
            # if it breaks then the boolean will be other string
            except ContainerFullException:
                boolean = 'error'
        if (method is 'M' and source != ''):
            curr = source[0]
            # delete the first character in source
            source = source[1:]
            result += curr
        if (method is 'G'):
            try:
                curr = container.peek()
                container.get()
                result += curr
            except ContainerEmptyException:
                boolean = 'error'
    # move cannot be the last method
    # container must be empty
    # result must reach the goal
    # the method should not cause error
    if (container.is_empty and result == goal and moves[-1] != 'P' and
            type(boolean) is bool and len_source == times):
        boolean = True
    else:
        boolean = False
    return boolean
