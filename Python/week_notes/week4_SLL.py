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
        return "(" + str(self._element) + ", " + str(hex(id(self._next))) + ")"
class SingleLinkedList():
    ''' represents a single linked list'''
    def __init__(self):
        '''(SingleLinkedList) ->NoneType
        initializes the references of an empty SLL'''
        self._size = 0
        self._head = None
        self._tail = None
    def set_head(self, new_head):
        '''(SingleLinkedList) -> None
        updates the head'''
        self._head = new_head
    def set_tail(self, new_tail):
        '''(SingleLinkedList) -> None
        updates the tail'''
        self._tail = new_tail
    def get_head(self):
        '''(SingleLinkedList) -> Node
        Return the pointer to the head'''
        return self._head 
    def get_tail(self, new_tail):
        '''(SingleLinkedList) -> Node
        Return the pointer to the tail'''
        return self._tail
        
    def is_empty(self):
        '''(SingleLinkedList) -> bool
        returns true if no item is in this SLL'''
        return self._size == 0
    
    def size(self):
        '''(SingleLinkedList) -> int
        returns the number of items in this SLL'''
        return self._size
    
    def add_first(self, element):
        '''(SingleLinkedList, obj) -> NoneType
        adds a node to the first of the SLL'''
        # create a node that point to the head
        node = Node(element, self._head)
        # let head point to the node
        self._head = node
        # if this node is the first node in this SLL, tail should point to this node too
        if (self._size == 0):
            self._tail = node
        # increment the size
        self._size += 1
   
    def add_last(self, element):
        '''(SingleLinkedList, obj) -> NoneType
        adds a node to the end of this SLL'''
        # create a node with the given element that points to None
        node = Node(element, None)
        # let the _next part of the tail to point to newly created node
        self._tail.set_next(node)
        #let tail to point to the added node
        self._tail = node
        # if this node is the first node in this SLL, let head to point to this node too
        if (self._size == 0):
            self._head = node
        # increment the size
        self._size += 1
        
    def remove_first(self):
        '''(SingleLinkedList, obj) -> obj
        remvoe the node from the head of this SLL and returns the element stored in this node'''
        # sset element to None in case SLL was empty
        element = None
        # if SLL is not empty
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
            
    def __str__(self):
        '''(SingleLinkedList) -> str
        returns the items in the SLL in a string form
        '''
        # define a node, which points to the head
        cur = self._head
        # define an empty string to be used as a container for the items in the SLL
        result = ""
        # loop over the SLL until you get to the end of the SLL
        while (cur is not None):
            # get the element that of the current node and attach it to the final result
            result = result + str(cur.get_element())  + ", "
            # proceed to next node
            cur = cur.get_next()
        #enclose the result in a parantheses
        result = "(" + result[:-2] + ")"
        #return the result
        return result

    def clear(self):
        '''(SingleLinkedList) -> None
        removes all the nodes'''
        # let cur point to head
        cur = self._head
        #travers the SLL while you get to the end
        while (cur is not None):
            #get the next node after the cur
            cur_next = cur.get_next()
            #have cur's next to point to None
            cur.set_next(None)
            #have cur point to the next available node
            cur = cur_next
        # have head and tail to point to null
        self._head = None
        self._tail = None

    def copy(self):
        '''(SingleLinkedList) -> SingleLinkedList
        creates a shallow copy of the SLL'''
        #ok guys, I, Marzieh, confess that I didn't have enough time to test this function
        #thoroughly. It's 2:11am and I'm sleepy and I have many other codes to write
        #so test it for me and see if it actually creates a "shallow" copy :)
        
        # create a new SLL
        new_list = SingleLinkedList()
        # if the current list is not empty
        if (not self.is_empty()):
            #update the new lists head to contain the 'element' and 'next' value of the original list. 
            new_list.set_head(Node(self._head.get_element(), self._head.get_next()))
            #call the new list's head new_cur to help traverse the new list
            new_cur = new_list.get_head()
            #let cur point to the next node of the original SLL
            cur = self._head.get_next()
            #travers the SLL to copy each node, advance until cur is none
            while (cur is not None):
                # copy the element and the _next value of the cur to the new node in new list
                new_cur.set_next(Node(cur.get_element(), None))
                #move one step forward
                new_cur = new_cur.get_next()
                # move forward the cur one step
                cur = cur.get_next()
            # set the tail of the new list
            new_list.set_tail(new_cur)
        #return the SLL
        return new_list

    def count(self, item):
        '''(SingleLinkedList, obj) -> int
        counts the number of occurrence of a value'''
        # let cur point to the head
        cur = self._head
        # initilaize a counter
        counter = 0
        # loop over the SLL until you get to the end
        while (cur is not None):
            # check if the element in the node is the same as the input item
            if (cur.get_element() == item):
                #incremetn the counter
                counter +=1
            # proceed the pointer
            cur = cur.get_next()
        # return the counter
        return counter

    def index(self, item):
        '''(SingleLinkedList, obj) -> int
        returns first index of that item was found'''
        # let cur point to the head
        cur = self._head
        # initilaize a counter
        counter = 0
        # set a flag to help exit the loop 
        flag = True
        # loop over the SLL until you get to the end or find the item
        while (cur is not None and flag ):
            # check if the element in the node is the same as the input item
            if (cur.get_element() == item):
                #incremetn the counter
                counter +=1
                flag = False
            # proceed the pointer
            cur = cur.get_next()
        # if flag is true, it means we get to the end of the list and didn't find the item so in this case raise ValueError
        if (flag):
            raise ValueError("item was not found")
        # return the counter
        return counter
    
    def insert(self, index, item):
        '''(SingleLinkedList, int, obj) -> NoneType
        insert item at the given index. if index > size, it insert_last, 
        if index <0 insert_first()'''
        #check if index > size -1 
        if(index > self._size - 1):
            # add to the end of the list (i.e. add_last())
            self.add_last(item)          
        #check if index < 0
        elif (index <= 0):
            # add to the front of the list (i.e. add_first)
            self.add_first(item)
        # otherwise traverese the list to insert it in the right place 
        else:
            #start from the head
            cur = self._head
            #initialize counter to zero
            counter = 0
            #loop over the list to get to index - 1
            while (counter != index -1 ):
                #proceed to next node
                cur = cur.get_next()
                #increment the counter 
                counter += 1
            #now you are in right point, insert the node by creating a new nodes
            new_node = Node(item, cur.get_next())
            #set current node to point to new node
            cur.set_next(new_node)

    def pop(self, index):
        '''(SingleLinkedList, int) -> obj
        remvoe the node from the list at the given index and returns the element stored in this node
        Raises IndexError if list is empty or index is out of range'''
        #check for the exception, if index is out of range or list is empty.
        if ( index <0 or index > self._size - 1 or self.is_empty()):
            raise IndexError("Invalid request")
        #if index point to the head (i.e. ==0)
        if (index == 0):
            # call remove_first and get the return element. We don't need to decrement the size here,
            #because remove_first does that for us
            element = self.remove_first()
        else:
            # create a pointer to point to the head
            cur = self._head
            # loop over the list 0< i < index-1 to get to one node before the one that is deleted 
            for i in range(0, index -1 ):
                # move one step forward
                cur = cur.get_next()
            #get the node to be deleted 
            node_to_delete = cur.get_next()
            #get its element to return
            element = node_to_delete.get_element()
            #link the current node to the node after the one that is deleted
            cur.set_next(node_to_delete.get_next())
            #nullify the node at the given index to make sure it is collected by GC
            node_to_delete.set_next(None)      
            # decrement the size
            self._size -= 1
        #return the element of the removed node
        return element

if (__name__ == "__main__"):       
     
    my_ll = SingleLinkedList()
    
    my_ll.add_first("A")
    my_ll.add_last("B")
    my_ll.add_first("C")
    my_ll.add_last("B")
    my_ll.add_last("D")
    my_ll.add_last("B")
    
    print(my_ll.count("B"))
    
    #my_ll.clear()
    #print(my_ll)
    
    new_ll = my_ll.copy()
    print(my_ll)
    #lets change the original list
    my_ll.remove_first()
    print(my_ll)
    print(new_ll)
    
    
    
    print(my_ll.index("B"))
    # expect to catch an exception because AA is not in the list
    #print(my_ll.index("AA"))
                
            
    print(my_ll)
    print(my_ll.size())
    my_ll.insert(6, "E")
    
    my_ll.insert(-2, "Q")
    my_ll.insert(0, "W")
    my_ll.insert(3,"R")
    print(my_ll)
    
    print(my_ll)
    print(my_ll.pop(0))
    print(my_ll)
    print(my_ll.pop(my_ll.size() - 1))
    print(my_ll)
    print(my_ll.pop(2))
    print(my_ll)
    # this should throw an excception
    #print(my_ll.pop(my_ll.size()))
    


        
        









