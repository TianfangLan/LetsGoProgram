from week4_DLL import DNode, DoubleLinkedList


def reverse_merge(DLL1, DLL2):
    '''(dll, dll) -> dll
    the function will take two double linked lists and merge them into
    one.
    '''
    # create the returning link list.
    re_dll = DoubleLinkedList()
    # loop until the elements in DLL1 is empty
    while (not DLL1.is_empty() or not DLL2.is_empty()):
        # get the nodes of very first names
        name1 = DLL1.get_first()
        name2 = DLL2.get_last()
        # get the element from the nodes
        name1 = name1.get_element()
        name2 = name2.get_element()
        # when the students register in both lecs
        if (name1 == name2):
            DLL2.remove_last()
            # add the name to re_list.
            re_dll.add_last(DLL1.remove_first())
        # if name1 does not equals to name2
        elif (name1 is not None and name2 is not None and name1 > name2):
            # add the smaller names to the end of the link list
            re_dll.add_last(DLL2.remove_last())
        elif (name1 is not None and name2 is not None and name1 < name2):
            # add the smaller names to the end of the link list
            re_dll.add_last(DLL1.remove_first())
        # if name1 is none means the dll1 is empty
        elif (name1 is None and name2 is not None):
            re_dll.add_last(DLL2.remove_last())
        # if name2 is none means dll2 is empty
        elif (name1 is not None and name2 is None):
            re_dll.add_last(DLL1.remove_first())
    return re_dll


def allocate_room(DLL, room, capacity, index):
    ''' (dll, str, int, int) -> str
    the function will take in a dll, room number, capacity and the index of
    the node contains the first person that is assigned to this room. Then
    return the first two letters of the surnames of the first and last person
    in the room.
    >>> allocate_room(csca48_list, 'SW319', 80, 150)
    SW319 JU-MO
    '''
    # set a current index
    cur_index = 0
    while (cur_index <= index):
        # get the current node
        cur = DLL.get_first()
        cur_element = cur.get_element()
        if (cur_element is not None):
            # remove and get the first name of the list
            cur_name = DLL.remove_first()
            cur_name = cur_name[0:2]
            cur_index += 1
        elif (cur_element is None):
            cur_index = index + 1
            cur_name = None
        first_name = str(cur_name)
    first_node = DLL.get_first()
    first_element = first_node.get_element()
    # set a counter
    counter = 0
    # the first person is one of the student in the class
    # need to do less than capacity - 1 not less and equal
    if (first_element is None or capacity is 1):
        last_name = first_name
    elif (capacity == 0):
        first_name = str(None)
        last_name = str(None)
    else:
        while (counter < capacity - 1):
            cur1 = DLL.get_first()
            # set the next node
            nex_element = cur1.get_next()
            # check cur1 is the last node or not
            if (nex_element is not None):
                cur1_name = DLL.remove_first()
                cur1_name = cur1_name[0:2]
            counter += 1
            last_name = cur1_name
            last_name = str(last_name)
    result = room + ' ' + first_name.upper() + '-' + last_name.upper()
    return result
