from week4_SLL import *
class HashTable():
    ''' A very basic hash table that stores integer numbers assuming that 
    collision never happens!'''
    def __init__(self, n):
        '''(HashTable, int) ->NoneType
        creates an empty list of length n'''
        self._array = [None]*n
        self._length = n 
    def put(self, data):
        '''(HashTable, int) -> NoneTye
        insert data in aelf._array'''
        self._array[self._hash_func(data)] = data
    def get(self, data): 
        '''(HashTable, int) -> bool
        returns True if data is found'''
        return self._array[self._hash_func(data)] == data
    def find(self, data): 
        '''(HashTable, int) -> int
        returns the index in which data is found
        otherwise returns -1'''
        index = self._hash_func(data)
        if (self._array[index] == data):
            result = index
        else: 
            result = -1
        return result
    def remove(self, data): 
        '''(HashTable, int) -> bool
        returns True if data was found and removed
        otherwise returns false'''
        index = self._hash_func(data)
        if (self._array[index] == data):
            self._array[index] = None
            result = True
        else: 
            result = False
        return result
   
    def _hash_func(self, data): 
        '''(HashTable, int) -> int
        returns the index in which data should be stored
        this method is supposed to be a private method therfore its name starts 
        with underscore'''
        return data%self._length
    def __str__(self):
        '''(HashTable)->str
        prints the content of the array'''
        result = ""
        for item in self._array:
            if item is not None: 
                result = result + "  "+ str(item)
        return "[" + result.strip() + "]"
            
class BucketArrayHashTable(HashTable):
    ''' A very basic hash table that stores objects in a hash table made of 
    bucket arrays'''
    
    def __init__(self, n):
        '''(HashTable, int) ->NoneType
        creates an empty list of length n 
        each list's index contains a pointer to an empty single linked list'''
        # create an empty list
        self._array = []
        # create n empty single linked list and get each cell of the _array to 
        # point to an empty single linked list 
        for i in range (n):
            sl = SingleLinkedList()
            self._array.append(sl) 
        # define _length to keep the size of the hash table
        self._length = n
    
    def put(self, data):
        '''(HashTable, int) -> NoneTye
        insert data in self._array
        since each cell of the _array points to list, data is actually added 
        to a single linked list'''
        # find the index in which the data should be inserted
        index = self._hash_func(data)
        # get the pointer to the single linked lists that is stored at that index
        pointer = self._array[index]
        #use SLL's add_first method to add the data to the list 
        pointer.add_first(data)
        
    def get(self, data): 
        '''(HashTable, int) -> bool
        returns True if data is found'''
        # find the index in which the data should be inserted        
        index = self._hash_func(data)
        # get the pointer to the single linked lists that is stored at that index
        pointer = self._array[index]
        # since we didn't define a get method for SLL, we implement it here. An awfully
        # bad practice!! The better design is to implement a get method inside SLL and then use it here.

        cur = pointer.get_head()
        flag = True
        while (cur is not None and flag ):
            if (cur.get_element() == data):
                flag = False
            cur = cur.get_next()
        if (flag):
            result = False
        else: 
            result = True

        return result        
    def find(self, data): 
        '''(HashTable, int) -> int
        returns the index in which data is found
        otherwise returns -1'''
        # if I don't override the method, the super method would be called and
        # will issue an error. 
        pass
    
    def remove(self, data): 
        '''(HashTable, int) -> bool
        returns True if data was found and removed
        otherwise returns false'''
        # find the index in which the data should be found
        index = self._hash_func(data)
        # get the pointer to the single linked lists that is stored at that index
        pointer = self._array[index]
        #use SLL's remove method to remove this data. but since we don't have remove method
        # for SLL, I'll leave it to you to complete. OR you can implemet the code here
        # just like what we've done in get method, which is not a good practice!
        pass
    
        
if (__name__ == "__main__"):
    hash_table = HashTable(10)
    hash_table.put(1)
    hash_table.put(10)
    hash_table.put(2)
    hash_table.put(5)
    hash_table.put(7)
    hash_table.put(3)
    hash_table.put(6)
    hash_table.put(4)
    hash_table.put(9)
    hash_table.put(8)
    print(hash_table)
    
    print(hash_table.find(10))
    print(hash_table.find(25))

    print(hash_table.get(10))
    print(hash_table.get(25))
    
    print(hash_table.remove(5))
    print(hash_table)

    
    ba = BucketArrayHashTable(10)
   
    ba.put(1)
    ba.put(10)
    ba.put(2)
    ba.put(5)
    ba.put(7)
    ba.put(3)
    # these two create a collision!
    ba.put(6)
    ba.put(16)

    ba.put(4)
    ba.put(9)
    # collision!
    ba.put(8)
    ba.put(28)
    
    '''
    # here I create the worst case scenario
    ba.put(1)
    ba.put(11)
    ba.put(21)
    ba.put(31)
    '''
    print(ba)  
    print(ba.get(16))
    print(ba.get(26))
 