from abc import ABC, abstractmethod
class EmptyQueueException(Exception):
    pass
class EmptyStackException(Exception):
    pass
class Container(ABC):
    def __init__():
        '''(Container) -> NoneType
        Create a new empty container
        '''
    @abstractmethod
    def put(self, element):
        '''(Container, obj) -> NoneType
        Add new_object to this container
        '''
    @abstractmethod
    def get(self):
        '''(Container) -> obj
        Remove and return an object (order not guarnteed) from this container
        '''
    def is_empty(self):
        '''(Container) -> bool
        Return True if this container is empty
        '''


class Queue(Container):
    ''' this class defines a Queueu ADT and raises an exception in case the queue is empty and dequeue() or front() is requested'''
    def __init__(self):
        '''(Queue) -> Nonetype
        creates an empty queue'''
        # representation invariant
        #_queue is a dictionary of int:obj
        #_next and _first are ints
        #_next - _first = the number of elements in the queue  
        # if _next > _first then 
        #     _queue[first], _queue[first+1], ...._queue[_next-1], _queue[_next] are the elements in the order
        #      they were inserted.
        self._queue = {}
        self._next = 0
        self._first = 0
        
    def put(self, element):
        '''(Queue, obj) -> NoneType
        insert and element to the back of this queue'''
        self.enqueue(element)
    
    def get(self):
        '''(Queue)->NoneType
        remove and returns one item from the front of the queue'''
        return self.dequeue()
    
    def enqueue(self, element):
        ''' (Queue, obj) -> NoneType
        add element to the back of the queue'''
        # The element goes to the back of queue
        self._queue[self._next] = element
        self._next += 1
        
    def dequeue(self):
        '''(Queue) -> obj
        remove and returns the element at the front of the queue
        raise an exception if _queue is empty'''
        if self.is_empty(): 
            raise EmptyQueueException ("This queue is empty")
        #remove and return the item at the front
        front = self._queue[self._first]
        self._queue.pop(self._first)
        self._first += 1
        return front

    def is_empty(self):
        ''' (Queue) -> bool
        returns true if _queue is empty'''
        return self._next - self._first == 0

    def size(self):
        '''(Queue) -> int
        returns the number of elements, which are in _queue'''
        return self._next - self._first

    def front(self):
        '''(Queue) -> obj
        returns the first element, which is in _queue
        It raises an exception if this queue is empty'''
        if (self.is_empty()):
            raise EmptyQueueException("This Queue is Empty")
        return self._queue[self._first]



class Stack(Container):
    ''' this class defines a FILO stack of items and raise an exception in case the Stack is empty wher pop() or top() is requested'''
    def __init__(self):
        '''(Stack) -> Nonetype
        creates an empty stack'''
        # representation invariant
        #_stack is a list
        #if _stack is not empty then  
        #    _stack[0] referes to the front/head of the stack
        #    _stack[:] referes to the elements of the stack in the order of insertion
        self._stack = []
   
    def put(self, element):
        '''(Stack, obj) -> NoneType
        add element to the top of this stack'''
        self.push(element)
        
    def get(self):
        '''(Stack)->obj
        remove and return an item from top of this stack'''
        return self.pop()
    
    def push(self, element):
        ''' (Stack, obj) -> NoneType
        add element to the top of the stack'''
        # The element goes to the top of the stack
        self._stack.insert(0, element)
        
    def pop(self):
        '''(Stack) -> obj
        remove and returns the element at the ftop of the stack
        raise an exception if _stack is empty'''
        if self.is_empty(): 
            raise EmptyStackException ("This stack is empty")
        #remove and return the item at the top
        return self._stack.pop(0)

    def is_empty(self):
        ''' (Stack) -> bool
        returns true if _stack is empty'''
        return (len(self._stack) == 0)

    def size(self):
        '''(Stack) -> int
        returns the number of elements, which are in _stack'''
        return len(self._stack)
    def top(self):
        '''(Stack) -> obj
        returns the first element, which is in _queue
        It raises an exception if this queue is empty'''
        if (self.is_empty()):
            raise EmptyStackException("This Stack is Empty")
        return self._Stack[0]




my_queue = Queue()
my_queue.put("A")
my_queue.put("B")
print(my_queue._queue)
print(my_queue.get())
print(my_queue._queue)

my_stack = Stack()
my_stack.put("A")
my_stack.put("B")
print(my_stack._stack)
print(my_stack.get())
print(my_stack._stack)
