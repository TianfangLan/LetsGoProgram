class BT():
    ''' represents a binary tree using a list.
    it's not efficient to use this method of implementation 
    if the BT is not complete because memory storage would be wasted.
    This implementation however works for both complete and non-complete tree.
    Since we don't have an actual node (TNode or Dnode), we have to implement the 
    methods that we normally implement for nodes (e.g. is_right(), has_right() etc.)
    ''' 
    def __init__(self, root_data):
        '''(BT, obj) -> NoneType
        construct a binary tree with data as its root'''
        #representation invariant
        # _binary_tree is a list
        # _binary_tree[0] represents the root of the tree
        # _binary_tree[2*i + 1] represents the left child of the 
        #     node that stored at index i, if exists
        # _binary_tree[2*i + 2] represents the right child of the 
        #     node that stored at index i, if exists
        # _binary_tree[:] represents the result of traversing the tree by BFS, if not empty
        
        
        # append root_data to an newly created empty list.
        self._binary_tree = []
        self._binary_tree.append(root_data)


    def add_left(self, root_index, data):
        ''' (BT, int, obj) -> int
        add the given data as a left child of root_index
        and return the index of the new_node
        REQ: 0<=root_indexindex <len(binary_tree) '''
        # raise an IndexError if the given index contains None data
        # I don't need to check if it is out of range, because I have mentioned that in REQ
        if (self._binary_tree[root_index] is None):
            raise IndexError ("Invalid Index")
        # find the index of root_index's left child
        left_child_index = root_index* 2 + 1
        # if left child's index is out of range (i.e. >= size of the list)
        if (left_child_index >= len(self._binary_tree)):
            # add None as previous nodes value
            for i in range (len(self._binary_tree), left_child_index + 1):
                self._binary_tree.append(None)
        # add element as the left child of root_index
        self._binary_tree[left_child_index] = data
        #return the index that data is inserted
        return left_child_index
        
    def add_right(self, root_index, data):
        ''' (BT, int, obj) -> NoneType
        add the given data as a right child of root_index
        and returns the index of the new_node
        REQ: 0<=root_indexindex <len(binary_tree) '''
        # raise an IndexError if the given index contains None data
        # I don't need to check if it is out of range, because I have mentioned that in REQ
        if (self._binary_tree[root_index] is None):
            raise IndexError ("Invalid Index")
        
        # find the index of root_index's left child
        right_child_index = root_index* 2 + 2
        # if right child's index is out of range (i.e. >= size of the tree)
        if (right_child_index >= len(self._binary_tree)):
            # add None as previous nodes' value
            for i in range (len(self._binary_tree), right_child_index + 1):
                self._binary_tree.append(None)
        # add element as the left child of root_index
        self._binary_tree[right_child_index] = data
        #return the index that data is inserted
        return right_child_index
    
    def BFS(self):
        '''(BT) -> str
        traverse the tree in Breadth First search mehtod
        '''
        # remove all Nones from the list
        result = ""
        for item in self._binary_tree:
            if (item is not None):
                result = result + " " + str(item)
        return result

    def find(self, data):
        '''(BT, obj) -> int
        return the index of the first occurence of data.
        raise ValueError exception if data not found'''
        
        #since we are using list ADT, if the data is 
        # not found an exception is raised. otherwise the index of the data
        # is returned.
        try:
            index = self._binary_tree.index(data)
        except:
            raise ValueError("No such an item exists")
        return index
        
    def get_root(self):
        '''(BT) -> obj
        return the data stored in the root'''
        return self._binary_tree[0]
        
    def get_data(self, index):
        '''(BT, int) -> obj
        return the data stored at the given index
        REQ: 0<=index<len(self._binary_tree)'''
        return self._binary_tree[index]
         
    
    def get_parent(self, index):
        '''(BT, int) -> int
        return the index to the parent of the node at given index'''
        # parent is always (index-1)//2 (integer division, rounded down)
        return (index -1)//2  
    
    def get_left(self, root_index):
        '''(BT) -> int
        return the index in which the left child of the given node is/to-be stored
        '''
        return 2*root_index+1

    def get_right(self, root_index):
        '''(BT, int) -> int
        return the index in which the right child of the given node is/to-be stored
        '''
        return 2*root_index+2


    def set_left(self, root_index, data):
        '''(Bt, index, data) -> NoneType
        set the left child of root_index to given data'''
        
        self.add_left(root_index, data)

    def set_right(self, root_index, data):
        '''(Bt, index, data) -> NoneType
        set the right child of root_index to given data'''
        
        self.add_right(root_index, data)

    def has_left(self, index):
        '''(BT, int) -> bool
        returns true if this node has a left child'''
        # a node has a left child if index*2 + 1 is in valid range and 
        # contains no None data
        return ((index*2 + 1) < len(self._binary_tree) and self._binary_tree[index* 2+ 1] is not None)
    
    def has_right(self, index):
        '''(BT, int) -> bool
        returns true if this node has a right child'''
        # a node has a right child if index*2 + 2 is in valid range and 
        # contains no None data
        return ((index*2 + 2) < len(self._binary_tree) and self._binary_tree[index* 2+ 2] is not None)

    def is_left(self, index):
        '''(BT, int) -> bool
        returns true if this index is a left child of its parent
        REQ: 0<= index < len(self._binary_tree)'''
        # a left child is stored at an odd index
        return (index % 2 != 0)

    def is_right(self, index):
        '''(BT, int) -> bool
        returns true if this index is a right child of its parent
        REQ: 0<= index < len(self._binary_tree)'''
        # a right child is stored at an odd index
        # becareful about root, which is at index 0
        return (index % 2 == 0 and index != 0)

    def is_root(self, index):
        '''(BT, int) -> bool
        returns true if the given index is the index of the root '''
        return (index == 0)
    
    

if (__name__ == "__main__"):
    ''' construct this tree
                 A
               /   \
             B      C   
            /\       \
           D  E      F
                    /
                   G
    '''
    bt = BT("A")
    node_B = bt.add_left(0, "B")
    node_c = bt.add_right(0, "C")
    bt.add_left(node_B, "D")
    bt.add_right(node_B, "E")
    node_F = bt.add_right(node_c, "F")
    bt.add_left(node_F, "G")
    
    print(bt.BFS())
    
    print(bt.find("G"))
    # print(bt.find("M"))  <- This will throw ValueError Exception
    
    print(bt.get_root())
    print(bt.get_data(bt.find("D")))
    print(bt.get_parent(bt.find("D"))) 
    # print(bt.get_parent(bt.find("M")))  <- 'M' does not exist so we expect an exception to be raised.
    print(bt.get_data(bt.get_left(bt.find("D")))) #<- get the left child of D (D does not have a left child)
    print(bt.get_data(bt.get_right(bt.find("A"))))
    bt.set_left(bt.find("A"), "M")
    bt.set_right(bt.find("A"), "N")
    print(bt.BFS())
    print(bt.has_right(bt.find("A")))
    print(bt.has_right(bt.find("F")))
    print(bt.is_right(bt.find("A")))
    print(bt.is_left(bt.find("M")))
    print(bt.is_root(bt.find("A")))
    # bt.add_left(1000, "Useless") <-raises an exception becuase index 1000 cannot be a parent (None data)
   
    
    