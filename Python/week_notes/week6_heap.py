class EmptyHeapException(Exception):
    pass
class Heap():
    ''' represents a heap, which is a complete binary tree, and satisfies 
    a heap-order, using a list.
    In this implelmentation, each node contains the keys only. 
    you complete this code by storing an entry (key, value) in each node.
    ''' 
    def __init__(self, root_data):
        '''(eah, obj) -> NoneType
        construct a heap with data as its root'''
        #representation invariant
        # _heap is a list
        # _heap[0] represents the root of the tree
        # _heap[0] has the highest priority
        # _heap[2*i + 1] represents the left child of the 
        #     node that stored at index i, and _heap[2*i + 1] >= _heap[i] 
        # _heap[2*i + 2] represents the right child of the 
        #     node that stored at index i, and _heap[2*i + 2] >= _heap[i]
        # _heap[len(_heap) -1] shows the last node
        # _heap[:] represents the result of traversing the tree by BFS, if not empty
        
        
        # append root_data to a newly created empty list.
        self._heap = []
        self._heap.append(root_data)
    
    def size(self):
        '''(Heap) -> int
        returns the number of nodes in the heap'''
        return len(self._heap)

    def is_empty(self):
        '''(Heap) -> bool
        returns True if this heap is empty'''
        return len(self._heap) == 0

    def remove_last_node(self):
        '''(Heap) -> obj
        removes the last node from the heap and returns the key stored in this node
        Raises: EmptyHeapException if this heap is empty'''
        if (self.is_empty()):
            raise EmptyHeapException("Heap is empty")
        return self._heap.pop(len(self._heap)-1)
    
    def min(self):
        '''(Heap) -> obj
        returns the item with the highest priority
        Raises: EmptyHeapException'''
        if (self.is_empty()):
            raise EmptyHeapException("Heap is empty")
        return self._heap[0]

    def insert(self, data):
        '''(Heap, obj) -> NoenType
        insert the given data at right place in the heap'''
        # step 1, 2, 3:  find the new last node, insert data, update last node
        # new last node is the element at len(self._heap)
        self._heap.append(data)
        #step 3, restore heap-order
        self.upheap_bubbling()
    def upheap_bubbling (self):
        '''(Heap) -> None
        restores heap order by swaping the items along an upward path from inserted node'''
        # find the last node index
        cur = len(self._heap)-1
        # find the parent (always  (last_node - 1//2) because it rounded down)
        parent = (cur -1 )//2
        # continue swapping until last node in right place or you get to the root
        while (cur > 0 and self._heap[parent] > self._heap[cur]):
            self._heap[parent] , self._heap[cur] = self._heap[cur] , self._heap[parent]
            # update cur and parent
            cur = parent
            parent = (cur -1 )//2
            
    def extract_min(self):
        '''(Heap) -> obj
        removes the highest priority item and return it.
        Raises: EmptyHeapException
        '''
        # raise an exception if heap is empty
        if (self.is_empty()):
            raise EmptyHeapException ("Heap is empty")
        # step 1: get the min value 
        min_value = self._heap[0]
        # remove the last node
        l_node = self._heap.pop(len(self._heap) -1)
        # step2: replace the root with last node if at least there is one item in the heap
        if(len(self._heap) != 0):
            # replace root with the last node
            self._heap[0] = l_node
            # step 3, 4: last node will be updated automatically, so restore the heap_order
            self.downheap_bubbling()
        # return the highest priority item
        return min_value
    
    def downheap_bubbling(self):
        '''(Heap) -> NoneType
        restore the heap order by swapping the items down the path'''
        # start from the root
        cur = 0
        # continue going down while heap order is violated
        while (self.violates(cur)):
            # find the index of the child which contains smaller data/ violates heap order
            child_index = self.find_index(cur)
            # swap data at cur and data at child
            self._heap[cur] , self._heap[child_index] = self._heap[child_index] , self._heap[cur]
            # update cur to point to child_index
            cur = child_index
    def violates(self, index):
        '''(Heap, index) -> bool
        checks if the given index has a key greater than one of its children'''
        # get left and right child index
        left = index * 2 + 1
        right = index * 2 + 2
        # raise a flag as an indicator of the violation
        violates = True
        # if cur index points to a leaf, it does not violate the heap order. a leaf is a node whose left child index is greater than the heap's length
        if (left >= len(self._heap)):
            violates = False
        # otherwise, it may have one child. since the heap is a complete tree, therfore it has a left child, which means the index to right child is >= than the heap's length. In this case we check the left child for the violation of heap-order
        elif (right >= len(self._heap)):
            violates = self._heap[index] > self._heap[left]
        #otherwise, it has two children, therefore you need to check both the children 
        else:
            violates = (self._heap[index] > self._heap[left]) or (self._heap[index] > self._heap[right])
        return violates
    def find_index(self, index): 
        '''(Heap, int) -> int
        return the index where it violates the heap order'''
        # find left and right child and initialize returned index
        left = index * 2 + 1
        right = index * 2 + 2
        returned_index = 0
        #if it has one child, it is left child. which means right child's index >= len of heap
        if (right >= len (self._heap)):
            returned_index = left
        # otherwise, we should find which one of its children has smaller data
        elif (self._heap[left] < self._heap[right]):
            returned_index = left
        else:
            returned_index = right
        #return the found index
        return returned_index
        
    def BFS(self):
        '''(BT) -> str
        traverse the tree in Breadth First search mehtod
        '''
        # remove all Nones from the list
        result = ""
        for item in self._heap:
            if (item is not None):
                result = result + " " + str(item)
        return result
        
        

    

    
    

if (__name__ == "__main__"):
    ''' construct  a priority queue using a heap
    containing these keys:
    95, 40, 55, 60, 20, 50, 85
    '''
    heap = Heap(95)
    heap.insert(40)
    heap.insert(55)
    heap.insert(60)
    heap.insert(20)
    heap.insert(50)
    heap.insert(85)
        
    print(heap.BFS())
    
    print(heap.extract_min())
    print(heap.BFS())
    print(heap.extract_min())
    print(heap.BFS())
    print(heap.extract_min())
    print(heap.BFS())
    print(heap.extract_min())
    print(heap.BFS())
    print(heap.extract_min())
    print(heap.BFS())
    print(heap.extract_min())
    print(heap.BFS())
    print(heap.extract_min())
    print(heap.BFS())
    """this should raise an exception
    print(heap.extract_min())
    """
