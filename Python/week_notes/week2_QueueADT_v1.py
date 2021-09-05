class EmptyQueueException(Exception):
    pass
class Queue():
    ''' this class defines a Queueu ADT and raises an exception in case the queue is empty and dequeue() or front() is requested'''
    def __init__(self):
        '''(Queue) -> Nonetype
        creates an empty queue'''
        # representation invariant
        #_queue is a list
        #if _queue is not empty then  
        #    _queue[0] referes to the front/head of the queue
        #    _queue[-1] referes to the back/tail of the queue
        #    _queue[:] referes to the elements of the queue in the order of insertion
        self._queue = []
    def enqueue(self, element):
        ''' (Queue, obj) -> NoneType
        add element to the back of the queue'''
        # The element goes to the back of queue
        self._queue.append(element)
        
    def dequeue(self):
        '''(Queue) -> obj
        remove and returns the element at the front of the queue
        raise an exception if _queue is empty'''
        if self.is_empty(): 
            raise EmptyQueueException ("This queue is empty")
        #remove and return the item at the front
        return self._queue.pop(0)
    def is_empty(self):
        ''' (Queue) -> bool
        returns true if _queue is empty'''
        return (len(self._queue) == 0)
    def size(self):
        '''(Queue) -> int
        returns the number of elements, which are in _queue'''
        return len(self._queue)
    def front(self):
        '''(Queue) -> obj
        returns the first element, which is in _queue
        It raises an exception if this queue is empty'''
        if (self.is_empty()):
            raise EmptyQueueException("This Queue is Empty")
        return self._queue[0]