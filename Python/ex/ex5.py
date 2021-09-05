from week6_heap import Heap, EmptyHeapException


def merge_heap(heap1, heap2):
    '''(Heap, Heap) -> Heap
    the function will take two heaps and merge them into one.
    '''
    # create the heap1 for returning
    item1 = None
    item2 = None
    try:
        item1 = heap1.remove_last_node()
    except:
        item1 = None
    try:
        item2 = heap2.remove_last_node()
    except:
        item2 = None
    if (item1 is None):
        re_heap = Heap(item2)
    elif (item2 is None):
        re_heap = Heap(item1)
    elif (item1 >= item2):
        re_heap = Heap(item2)
        re_heap.insert(item1)
    else:
        re_heap = Heap(item1)
        re_heap.insert(item2)
    # keep extract heap2 until it is empty
    while (not heap1.is_empty() or not heap2.is_empty):
        try:
            item1 = heap1.remove_last_node()
        except:
            item1 = None
        try:
            item2 = heap2.remove_last_node()
        except:
            item2 = None
        if (item1 is None and item2 is not None):
            re_heap.insert(item2)
        elif (item2 is None and item1 is not None):
            re_heap.insert(item1)
        elif (item1 >= item2):
            re_heap.insert(item1)
            re_heap.insert(item2)
        else:
            re_heap.insert(item2)
            re_heap.insert(item1)
    return re_heap


def first_and_last(heap):
    ''' (Heap) -> tuple
    the function will take a heap in and return the surename of the first
    and the last student in the form of tuple
    '''
    # try to return and lose the first name
    try:
        first = heap.extract_min()
    # if the heap is empty return none
    except EmptyHeapException:
        first = None
    # create the last name
    last = first
    # get the size of the heap
    size = heap.size()
    while (not heap.is_empty()):
        # keep losing the smallest surename
        # the last one been lost is the biggest one
        last = heap.extract_min()
    result = (first, last)
    return result
