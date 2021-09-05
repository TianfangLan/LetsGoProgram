class EmptyPriorityQueueException(Exception):
    pass
class Entry():
    ''' represents an entry that includes a key and a value'''
    def __init__(self, key, value):
        '''(Item, int, obj) -> NoneType
        constructs an item using key and value'''
        #repersentation invariant
        #_key is a posititve integer
        #_value is an object of any type
        self._key = key
        self._value = value
    def get_key(self):
        '''(Entry) ->int
        returns the key of this entry'''
        return self._key
    
    def get_value(self):
        '''(Entry) ->obj
        returns the value of this entry'''
        return self._value
    
    def __str__(self):
        '''(Entry) ->str
        returns a string representation  of this entry'''
        return "("+str(self._key)+", "+ str(self._value) + ")"

class PriorityQueue_1():
    '''represents a PQ ADT implemented with an "unsorted list" '''
    def __init__(self):
        '''(PriorityQueue_1) ->NoneType
        constructs an empty PQ'''
        #repersentation invariant
        #self._pq is a list
        #if self._pq is not empty
        #     self._pq[:] shows the items in the PQ
        #     self._pq[-1] shows the most recent item that's been added
        self._pq = []
    
    def is_empty(self):
        '''(PriorityQueue_1) ->boolean
        returns true if the PQ is empty'''
        return len(self._pq) == 0
    
    def size(self):
        '''(PriorityQueue_1) ->int
        returns the size of the PQ'''
        return len(self._pq)
    
    def insert(self, element, priority):
        '''(PriorityQueue_1, obj, int) ->NoneType
        insert an entry to the PQ, whose key = priority and value = element
        REQ: priority >=0'''
        # create an entry
        entry = Entry(priority, element)
        # add it the end of the PQ
        self._pq.append(entry)
        
    def min(self):
        '''(PriorityQueue_1) ->NoneType
        returns the entry with the highest priority, raises an 
        exception if the PQ is empty'''
        #raise an exception if the PQ is empty
        if (self.is_empty()):
            raise EmptyPriorityQueueException("This priority queue is empty")
        # get the first entry as the min entry
        min = self._pq[0]
        #find the entry with the highest priority and assign it to min
        for item in self._pq:
            if (item.get_key() < min.get_key()):
                min = item
        # return the entry with the highest priority(min)
        return min
   
    def extract_min(self):
        '''(PriorityQueue_1) ->obj
        returns and removes the entry with the highest priority, raises an 
        exception if the PQ is empty'''
        #raise an exception if the PQ is empty
        if (self.is_empty()):
            raise EmptyPriorityQueueException("This priority queue is empty")
        # assume the first entry has the highest priority
        min = self._pq[0]
        #keep track of the index of the entry with the highest priority
        removed_index = 0
        #find the entry with the highest priority and keep track of the index 
        #of the entry with the highest priority.
        for i in range(len(self._pq)):
            if (self._pq[i].get_key() < min.get_key()):
                min = self._pq[i]
                removed_index = i
        # remove and return the 
        return self._pq.pop(removed_index)
    def __str__(self):
        '''(PriorityQueue_1) -> str
        returns a string representing this PQ'''
        result = "{"
        for item in self._pq:
            result = result + item.__str__() + ", "
        result = result[:-2] + "}"
        return result
    
class PriorityQueue_2():
    '''represents a PQ ADT implemented with a "sorted list" '''
    def __init__(self):
        '''(PriorityQueue_2) ->NoneType
        constructs an empty PQ'''
        #repersentation invariant
        #self._pq is a list
        #if self._pq is not empty
        #     self._pq[:] shows the items in the PQ
        #     self._pq[-1] shows the item with the highest priority
        self._pq = []
    
    def is_empty(self):
        '''(PriorityQueue_2) ->boolean
        returns true if the PQ is empty'''
        return len(self._pq) == 0
    
    def size(self):
        '''(PriorityQueue_2) ->int
        returns the size of the PQ'''
        return len(self._pq)
    
    def insert(self, element, priority):
        '''(PriorityQueue_1, obj, int) ->NoneType
        insert an entry to the PQ, whose key = priority and value = element
        REQ: priority >=0'''
        # create an entry
        entry = Entry(priority, element)
        
        #if the PQ is empty add it to the list
        if (self.is_empty()):
            self._pq.append(entry)
        # otherwise, place the item in right place by comparing its key 
        #with the last entry's key in the PQ
        else:
            insert_index = 0
            found = False
            # find the right place for insertion by comparing the priority of the 
            # caurrent entry priority and the entries that are already in the PQ
            index = 0
            while (index < len(self._pq) and not found):
                # we use >= instead of > so that the if we have similar key, 
                #the most recent one amongst them, gets the least priority
                if (self._pq[index].get_key() < priority):
                    insert_index = index
                    found = True
                index+=1
            # insert the entry
            if (not found):
                self._pq.insert(len(self._pq), entry)
            else:
                self._pq.insert(insert_index, entry)
                
        
    def min(self):
        '''(PriorityQueue_2) ->NoneType
        returns the entry with the highest priority, raises an 
        exception if the PQ is empty'''
        #raise an exception if the PQ is empty
        if (self.is_empty()):
            raise EmptyPriorityQueueException("This priority queue is empty")
        # return the entry with the highest priority(min), which is at the end of the PQ
        return self._pq[len(self._pq) -1]
   
    def extract_min(self):
        '''(PriorityQueue_1) ->obj
        returns and removes the entry with the highest priority, raises an 
        exception if the PQ is empty'''
        #raise an exception if the PQ is empty
        if (self.is_empty()):
            raise EmptyPriorityQueueException("This priority queue is empty")
        # return ans remove the highest priority entry, which is at the end of the PQ
        return self._pq.pop(len(self._pq) -1)
    def __str__(self):
        '''(PriorityQueue_2) -> str
        returns a string representing this PQ'''
        result = "{"
        for item in self._pq:
            result = result + item.__str__() + ", "
        result = result[:-2] + "}"
        return result
        
print("\n Testing the first PQ, implemented using an unsorted list...")
my_pq = PriorityQueue_1()
print("Is the pq empty? " + str(my_pq.is_empty()))
my_pq.insert("A", 10)
my_pq.insert("B", 5)
my_pq.insert("C", 20)
my_pq.insert("D", 15)
print(my_pq)
print("What's the size of the pq ? " + str(my_pq.size()))
print("The highest priority item is" + str(my_pq.min()))
my_pq.extract_min()
print("The highest priority item is" + str(my_pq.min()))

print("\n Testing the second PQ, implemented using a sorted PQ...")
my_pq = PriorityQueue_2()
print("Is the pq empty? " + str(my_pq.is_empty()))
my_pq.insert("A", 10)
my_pq.insert("B", 5)
my_pq.insert("C", 20)
my_pq.insert("D", 15)
print(my_pq)
print("What's the size of the pq ? " + str(my_pq.size()))
print("The highest priority item is" + str(my_pq.min()))
my_pq.extract_min()
print("The highest priority item is" + str(my_pq.min()))


