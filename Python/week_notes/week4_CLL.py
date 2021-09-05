class EmptyCircularLinkedList():
    pass
class Node():
    '''represents a node as a building block of a single linked list'''
    def __init__(self, element, next_node=None):
        '''(Node, obj, Node) -> 
        construct a node as building block of a single linked list'''
        
        self._element = element
        self._next = next_node
    
    def set_next(self, next_node):
        '''(Node, Node) -> NoneType
        set node to point to next_node'''
        self._next = next_node
    
    def set_element(self, element):
        '''(Node, obj) ->NoneType
        set the _element to a new value'''
        self._element = element
    
    def get_next(self):
        '''(Node) -> Node
        returns the reference to next node'''
        return self._next
    
    def get_element(self):
        '''(Node) -> obj
        returns the element of this node'''
        return self._element
    
    def __str__(self):
        '''(Node) -> str
        returns the element of this node and the reference to next node'''
        return "(" + str(hex(id(self._next)))+ str(self._element) + ", " + str(hex(id(self._next))) + ")"
    
class CircularLinkedList():
    ''' represents a circular linked lists'''
    def __init__(self):
        '''(CircularLinkedList)->NoneType
        constructs a CLL by initializing its cursor and size'''
        self._cursor = None
        self._size = 0
    def is_empty(self):
        '''(CircularLinkedList) -> bool
        returns true if no item is in this CLL'''
        return self._size == 0
    
    def size(self):
        '''(CircularLinkedList) -> int
        returns the number of items in this SLL'''
        return self._size    
    def advance(self):
        '''(CircularLinkedList) -> NoneType
        advance the cursor one node'''
        self._cursor = self._cursor.get_next()
        
    def add(self, element):
        '''(CircularLinkedList, obj) -> NoneType
        add a node after the cursor'''
        # create a new node that point to None
        new_node = Node(element, None)        
        # if cursor is empty (the first node that is added)
        if (self._cursor is None):
            # call this new_node : cursor
            self._cursor = new_node
            # let cursor point to itself to make the list circular
            self._cursor.set_next(new_node)
        else:
            #the new node should point to the node, which is after the cursor
            new_node.set_next(self._cursor.get_next())
            #let the cursor point to the new node
            self._cursor.set_next(new_node)
        # advance the cursor
        self.advance()
        # increment the size
        self._size += 1
    def remove(self):
        '''(CircularLinkedList) -> obj
        removes the node after the cursor and returns the element stored in the node'''
        #raise an exception if CLL is empty
        if (self.is_empty()):
            raise EmptyCircularLinkedList("This CLL is empty")
        # if there is only one node in the CLL
        if(self._size == 1):
            # get the element at cursor 
            element = self._cursor.get_element()
            # Nullify the cursor
            self._cursor = None
        else:
            #find the node to be removed (one after the cursor)
            deleted_node = self._cursor.get_next()
            # get the node after the node that's going to be removed
            next_node = deleted_node.get_next()
            #link cursor and the node after removed node
            self._cursor.set_next(next_node)
            # get the element of the removed node
            element = deleted_node.get_element()
            #nullify the removed node
            deleted_node.set_next(None)      
        #decrement the size
        self._size -= 1
        #return the element
        return element
        
    
    def __str__(self):
        '''(CircularLinkedList) -> str
        returns the items in the CLL in a string form
        '''
        # define an empty string to be used as a container for the items in the CLL
        result = ""
        # if there are some nodes in the CLL
        if (not self.is_empty()):
            # define a node, which points to the node after the cursor
            # because cursor actually points to the tail of the list
            cur = self._cursor.get_next()
            # loop over the CLL until you get to the end of the CLL (i.e. cursor)
            while (cur is not self._cursor):
                # get the element that of the current node and attach it to the final result
                result = result + str(cur.get_element())  + ", "
                # move forward
                cur = cur.get_next()
                
            # now we got to cursor again, so we add its element to the result
            result = result + str(cur.get_element()) 
            #enclose the result in a parantheses
        result = "(" + result + ")"
        #return the result
        return result
        

if (__name__ == "__main__"):       
    cll = CircularLinkedList()
    cll.add("A")
    cll.add("B")
    cll.add("C")
    print(cll)
    
    #it's not a good idea to access a class instance variable directly,
    #but just to show you where cursor points to, excuste the following line
    print(cll._cursor.get_element())
    print(cll.remove())
    print(cll)
    print(cll.remove())
    print(cll)
    print(cll.remove())
    print(cll)
    print(cll.size())
    print(cll.is_empty())
