class DNode():
    '''represents a node as a building block of a double linked list'''
    def __init__(self, element, prev_node=None, next_node=None):
        '''(Node, obj, Node, Node) -> NoneType
        construct a Dnode as building block of a double linked list'''
        # Representation invariant:
        # element is an object, that is hold this node
        # _prev is a DNode
        # _next is a DNode
        # _prev is the node immediately before this node (i.e. self)
        # _next is the node immediately after this node (i.e. self)     
        
        self._element = element
        self._next = next_node
        self._prev = prev_node
    
    def set_next(self, next_node):
        '''(Node, Node) -> NoneType
        set node to point to next_node'''
        self._next = next_node
    
    def set_prev(self, prev_node):
        '''(Node, Node) -> NoneType
        set node to point to prev_node'''
        self._prev = prev_node

    def set_element(self, element):
        '''(Node, obj) ->NoneType
        set the _element to a new value'''
        self._element = element
    
    def get_next(self):
        '''(Node) -> Node
        returns the reference to next node'''
        return self._next
    
    def get_prev(self):
        '''(Node) -> Node
        returns the reference to previous node'''
        return self._prev

    def get_element(self):
        '''(Node) -> obj
        returns the element of this node'''
        return self._element
    
    def __str__(self):
        '''(Node) -> str
        returns the element of this node and the reference to next node'''
        return "(" + str(hex(id(self._prev)))+ ", "+ str(self._element) + ", " + str(hex(id(self._next))) + ")"

class DoubleLinkedList():
    ''' represents a double linked list'''
    def __init__(self):
        '''(DoubleLinkedList) ->NoneType
        initializes the references of an empty DLL'''
        #set the size
        self._size = 0
        #head and tails are a dummy node
        self._head = DNode(None, None, None)
        self._tail = DNode(None, None, None)
        #head points to tail and tail to head
        self._head.set_next(self._tail)
        self._tail.set_prev(self._head)
       
    def is_empty(self):
        '''(DoubleLinkedList) -> bool
        returns true if no item is in this DLL'''
        return self._size == 0
    
    def size(self):
        '''(DoubleLinkedList) -> int
        returns the number of items in this DLL'''
        return self._size
    def get_first(self):
        '''(DoubleLinkedList) -> Dnode
        return a pointer to the first node in the list if the list is not empty, 
        otherwise the pointer points to the (dummy) tail'''
        return self._head.get_next()
    def get_last(self):
        '''(DoubleLinkedList) -> Dnode
        return a pointer to the last node in the list if the list is not empty, 
        otherwise the pointer points to the (dummy) head'''
        return self._tail.get_prev()

    def add_first(self, element):
        '''(DoubleLinkedList, obj) -> NoneType
        adds a node to the front of the DLL, after the head'''
        # create a node that head points to. Also the node points to the node after the head 
        node = DNode(element, self._head, self._head.get_next())
        # have the node after head to point to this node (_prev)
        self._head.get_next().set_prev(node)
        #have the head to point to this new node 
        self._head.set_next(node)
        # increment the size
        self._size += 1
   
    def add_last(self, element):
        '''(DoubleLinkedList, obj) -> NoneType
        adds a node to the end of this DLL'''
        # create a DNode with the given element that points to tail from right and to the node before the tail from left
        node = DNode(element, self._tail.get_prev(), self._tail)
        #let the node to the left of the tail to point to this new node
        self._tail.get_prev().set_next(node)
        # let the _prev part of the tail to point to newly created node
        self._tail.set_prev(node)
        # increment the size
        self._size += 1
        
    def remove_first(self):
        '''(DoubleLinkedList, obj) -> obj
        remvoe the node from the head of this DLL and returns the element stored in this node'''
        # set element to None in case DLL was empty
        element = None
        # if DLL is not empty
        if (not self.is_empty()):
            # get the first node to the right of the head
            node = self._head.get_next()
            # have head point to the second node after the head
            self._head.set_next(node.get_next())
            #have the second node after the head to point to head from left
            node.get_next().set_prev(self._head)
            # decrement the size
            self._size -= 1
            #set the _next & _prev of the removed node to point to None (for garbage collection purpose)
            node.set_next(None)
            node.set_prev(None)
            # get the element stored in the node
            element = node.get_element()
        #return the element of the removed node
        return element
    def remove_last(self):
        '''(DoubleLinkedList, obj) -> obj
        remvoe the node from the tail of this DLL and returns the element stored in this node'''
        # set element to None in case DLL was empty
        element = None
        # if DLL is not empty
        if (not self.is_empty()):
            # get the first node to the left of the tail
            node = self._tail.get_prev()
            # have tail point to the second node before the tail
            self._tail.set_prev(node.get_prev())
            #have the second node before the tail to point to tail from right
            node.get_prev().set_next(self._tail)
            # decrement the size
            self._size -= 1
            # get the element stored in the node
            element = node.get_element()
            #Nullify the deleted node (for garbage collection purpose)
            node.set_next(None)
            node.set_prev(None)
        #return the element of the removed node
        return element
            
    def __str__(self):
        '''(DoubleLinkedList) -> str
        returns the items in the DLL in a string form
        '''
        # define a node, which points to the first node after the head
        cur = self._head.get_next()
        # define an empty string to be used as a container for the items in the SLL
        result = ""
        # loop over the DLL until you get to the end of the DLL
        while (cur is not self._tail):
            # get the element of the current node and attach it to the final result
            result = result + str(cur.get_element())  + ", "
            # proceed to next node
            cur = cur.get_next()
        #enclose the result in a parantheses
        result = "(" + result[:-2] + ")"
        #return the result
        return result




if (__name__ == "__main__"):        
    node_1 = DNode("A")
    node_2 = DNode("B", node_1)
    node_3 = DNode("C", node_1, node_2)
    print(node_1)
    print(node_2)
    print(node_3)
    print(str(hex(id(node_1))))
    print(str(hex(id(node_2))))
    dll = DoubleLinkedList()
    print(dll)
    dll.add_first("A")
    dll.add_first("B")
    dll.add_last("C")
    dll.add_last("D")   
    print(dll)
    print(dll.remove_last())
    print(dll.remove_last())
    print(dll.remove_last())
    print(dll.remove_last())
    print(dll)


