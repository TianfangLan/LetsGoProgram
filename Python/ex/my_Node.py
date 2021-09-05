from week3_node import node
class SingleLinkList():
    ''' represent a single link list'''
    def __init__(self):
        '''(SingleLinkList) -> NoneType
        initializes the reference of an empty SLL'''
        self._size = 0
        self._head = None
        self._tail = None
        
    def is_empty(self):
        ''' give back True if the link list is none'''
        return self._size == 0
    
    def get_size(self):
        return self._size

    def add_first(self, element):
        node = Node(element, self._head)
        self._head = node
        if(self._size == 0):
            self._tail = node
        self._size += 1

    def add_last(self, element):
        node = Node(element,None)
        self._tail = node
        if (self._size == 0):
            self._head = node
        self._size += 1

    def remove_first(self):
        element = None
        if (self._head is not None):
            node = self._head
            element = node.get_element()
            self._node = self._head.get_next()
            self._size -= 1
            node.set_next(None)
        return element

        
        
        