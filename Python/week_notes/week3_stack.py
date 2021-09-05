from week3_node import Node

class Stack():
    ''' represents a Stack implemented by a node list '''
    def __init__(self):
        '''(Stack) ->NoneType
        initializes the references of an empty Stack'''
        self._size = 0
        self._head = None
    
    def is_empty(self):
        '''(Stack) -> bool
        returns true if no item is in this Stack'''
        return self._size == 0
    
    def size(self):
        '''(Stack) -> int
        returns the number of items in this Stack'''
        return size
    
    def push(self, element):
        '''(Stack, obj) -> NoneType
        adds a node to the top of the Stack'''
        # create a node that point to the head
        node = Node(element, self._head)
        # let head point to the node
        self._head = node
        # increment the size
        self._size += 1
   
        
    def pop(self):
        '''(Stack, obj) -> obj
        remvoe the node from the top of this Stack and returns the element stored in this node'''
        # set element to None in case Stack was empty
        element = None
        # if Stack is not empty
        if (self._head is not None):
            # get the first node
            node = self._head
            # let head point to the second node
            self._head = self._head.get_next()
            # decrement the size
            self._size -= 1
            #set the _next of previous head to point to None (for garbage collection purpose)
            node.set_next(None)
            # get the element stored in the node
            element = node.get_element()
        #return the element of the removed node
        return element
            
    def top(self):
        '''(Stack, obj) -> obj
        returns the element stored in the top of the stack'''
        # set element to None in case Stack was empty
        element = None
        # if Stack is not empty
        if (self._head is not None):
            # get the element stored in the node
            element = self._head.get_element()
        #return the element of the removed node
        return element

    def __str__(self):
        '''(Stack) -> str
        returns the items in the Stack in a string form
        '''
        # define a node, which points to the head
        cur = self._head
        # define an empty string to be used as a container for the items in the Stack
        result = ""
        # loop over the SSL until you get to the end of the SSL
        while (cur is not None):
            # get the element that of the current node and attach it to the final result
            result = result + str(cur.get_element())  + ", "
            # proceed to next node
            cur = cur.get_next()
        #enclose the result in a parantheses
        result = "(" + result[:-2] + ")"
        #return the result
        return result


stack = Stack()
stack.push("A")
stack.push("B")
stack.push("C")
stack.push("D")
print(stack)
print(stack.top())
print(stack.pop())
print(stack)









