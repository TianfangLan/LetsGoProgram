class EmptyStackException(Exception):
    pass
class Stack():
    ''' this class defines a FILO stack of items and raise an exception in case the Stack is empty wher pop() or top() is requested'''
    def __init__(self):
        '''(Stack) -> Nonetype
        creates an empty stack'''
        # representation invariant
        #_stack is a list
        #if _stack is not empty then  
        #    _stack[0] referes to the top of the stack
        #    _stack[:] referes to the elements of the stack in the order of insertion
        self._stack = []
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