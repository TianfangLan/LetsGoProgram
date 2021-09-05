from week3_node import Node
class Queue():
    ''' represents a queue implemented by a node list'''
    def __init__(self):
        '''(Queue) ->NoneType
        initializes the references of an empty queue'''
        self._size = 0
        self._head = None
        self._tail = None
    
    def is_empty(self):
        '''(Queue) -> bool
        returns true if no item is in this queue'''
        return self._size == 0
    
    def size(self):
        '''(Queue) -> int
        returns the number of items in this queue'''
        return size
    
  
    def enqueue(self, element):
        '''(Queue, obj) -> NoneType
        adds a node to the end of this queue'''
        # create a node with the given element that points to None
        node = Node(element, None)
        # let the _next part of the tail to point to newly created node
        if (self.is_empty()):
            self._tail = node
        else:
            self._tail.set_next(node)
            #let tail to point to the added node
            self._tail = node
        # if this node is the first node in this queue, let head to point to this node too
        if (self._size == 0):
            self._head = node
        # increment the size
        self._size += 1
        
    def dequeue(self):
        '''(Queue, obj) -> obj
        remvoe the node from the head of this queue and returns the element stored in this node'''
        # set element to None in case queue was empty
        element = None
        # if queue is not empty
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

    def front(self):
        '''(Queue, obj) -> obj
        returns the element stored in the front of the queue'''
        # set element to None in case queue was empty
        element = None
        # get the element if the queue is not empty
        if (self._head is not None):
            element = self._head.get_element()
        #return the element of the removed node
        return element
            
    def __str__(self):
        '''(Queue) -> str
        returns the items in the queue in a string form
        '''
        # define a node, which points to the head
        cur = self._head
        # define an empty string to be used as a container for the items in the queue
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

queue = Queue()
queue.enqueue("A")
queue.enqueue("B")
queue.enqueue("C")
queue.enqueue("D")
print(queue)
print(queue.dequeue())
print(queue)
print(queue.front())
