from abc import ABC, abstractmethod


# Error classes
class ContainerFullException(Exception):
    def __init__(self):
        Exception.__init__(self)


class ContainerEmptyException(Exception):
    def __init__(self):
        Exception.__init__(self)


# Abstract base class as a frame for the other ADTs
class Container(ABC):
    def __init__(self):
        self._list = []

    # Mandatory methods for subclasses to implement
    @abstractmethod
    def put(self, item):
        ''' (Container, obj) -> NoneType
        Puts an item in the container.
        '''
        pass

    @abstractmethod
    def get(self):
        ''' (Container) -> obj
        Gets the first item in the container and also removes it from the
        container.
        '''
        pass

    @abstractmethod
    def peek(self):
        ''' (Container) -> obj
        Gets the first item in the container but does not remove it from the
        container.
        '''
        pass

    @abstractmethod
    def is_empty(self):
        ''' (Container) -> bool
        Returns whether or not the container is empty
        '''
        pass


# Stack class
class Stack(Container):
    ''' Represents a Stack data type. Last index is top of stack. '''
    def __init__(self):
        Container.__init__(self)

    def put(self, item):
        self._list.append(item)

    def get(self):
        if (len(self._list) == 0):
            raise ContainerEmptyException
        else:
            return self._list.pop(-1)

    def peek(self):
        if (len(self._list) == 0):
            raise ContainerEmptyException
        else:
            return self._list[-1]

    def is_empty(self):
        return len(self._list) == 0


# Queue class
class Queue(Container):
    ''' Represents a Queue data type. First index is the front of the queue.
    '''
    def __init__(self):
        Container.__init__(self)

    def put(self, item):
        self._list.append(item)

    def get(self):
        if (len(self._list) == 0):
            raise ContainerEmptyException
        else:
            return self._list.pop(0)

    def peek(self):
        if (len(self._list) == 0):
            raise ContainerEmptyException
        else:
            return self._list[0]

    def is_empty(self):
        return len(self._list) == 0


# Bucket class
class Bucket(Container):
    ''' Represents a Bucket data type, can only hold one item. '''
    def __init__(self):
        Container.__init__(self)

    def put(self, item):
        # Buckets can only hold one item, so throw error if full
        if (len(self._list) == 1):
            raise ContainerFullException
        else:
            self._list.append(item)

    def get(self):
        if (len(self._list) == 0):
            raise ContainerEmptyException
        else:
            return self._list.pop(0)

    def peek(self):
        if (len(self._list) == 0):
            raise ContainerEmptyException
        else:
            return self._list[0]

    def is_empty(self):
        return len(self._list) == 0