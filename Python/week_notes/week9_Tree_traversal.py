###### Definig a node for a binary tree ################
class BTNode():
    ''' a class that represents a binary tree node'''
    def __init__(self, data, parent=None, left_child=None, right_child=None):
        '''(BTNode, obj, BTNode, BTNode, BTNode) -> NoneType
        Constructs a binary tree nodes with the given data'''
        
        self._parent = parent
        self._left = left_child
        self._data = data
        self._right = right_child

    def set_parent(self, parent):
        '''(BTNode, BTNode) -> NoneType
        set the parent to the given node'''
        self._parent = parent
    def set_left(self, left_child):
        '''(BTNode, BTNode) -> NoneType
        set the left child to the given node'''
        self._left = left_child

    def set_right(self, right_child):
        '''(BTNode, BTNode) -> NoneType
        set the right child to the given node'''
        self._right = right_child
    def set_data(self, data):
        '''(BTNode, obj) -> NoneType
        set the data at this node to the given data'''
        self._data = data    

    def get_parent(self):
        '''(BTNode) -> BTNode
        return the pointer to the parent of this node'''
        return self._parent
    
    def get_left(self):
        '''(BTNode) -> BTNode
        return the pointer to the left child'''
        return self._left

    def get_right(self):
        '''(BTNode) -> BTNode
        return the pointer to the right child'''
        return self._right   
    def get_data(self):
        '''(BTNode) -> obj
        return the data stored in this node'''
        return self._data

    def has_left(self):
        '''(BTNode) -> bool
        returns true if this node has a left child'''
        return (self.get_left() is not None)
    def has_right(self):
        '''(BTNode) -> bool
        returns true if this node has a right child'''
        return (self.get_right() is not None)  
    def is_left(self):
        '''(BTNode) -> bool
        returns true if this node is a left child of its parent'''
        # you need to take care of exception here, if the given node has not parent
        return (self.get_parent().get_left() is self)
    def is_right(self):
        '''(BTNode) -> bool
        returns true if the given node is a right child of its parent'''
        # you need to take care of exception here, if the given node has not parent
        return (self.get_parent().get_right() is self)
    def is_root(self):
        '''(BTNode) -> bool
        returns true if the given node has not parent i.e. a root '''
        return (self.get_parent() is None)
    
    def is_leaf(self):
        '''(BTNode) -> bool
        returns true if the given node is a leaf '''
        return (not (self.has_right() or self.has_left()))
        
##### defining a binary tree ################
class BTree():
    ''' represents a binary tree'''
    def __init__(self, root):
        '''(BTree, BTNode, BTnode) -> NoneType
        construct a tree by creating a root 
        '''
        self._root = root
    def get_root(self):
        '''(BTree) -> BTNode
        return the pointer ot the root of this tree'''
        return self._root
    def add_left (self, node, data):
        '''(BTree, BTNode, obj) -> BTNode
        add a left child to the given node and return the pointer to this node'''
        new_node = BTNode(data, node)
        node.set_left(new_node)
        return new_node
    def add_right (self, node, data):
        '''(BTree, BTNode, obj) -> NoneType
        add a right child to the given node and return the pointer to this node'''
        new_node = BTNode(data, node)
        node.set_right(new_node)
        return new_node

    def in_order(self, node):
        '''(BTree, BTNode) -> NoneType
        visits all the nodes in the tree by in-order traversal method.
        REQ: node is not None
        '''
        
        # recursive case
        if (node.has_left()):
            self.in_order(node.get_left())
        #base case
        print(node.get_data(), " ", end="")
        #recursive case
        if(node.has_right()):
            self.in_order(node.get_right())
    
    # a better version of in-order traversal that fully covers the recursive 
    # definition of a tree, where it says a tree can be a None pointer...
    # please notice that this version takes in one more parameter (i.e. result)
    def in_order_(self, node, result= ''):
        '''(BTree, BTNode, str) -> NoneType
        visits all the nodes in the tree by in-order traversal method.
        REQ: node is not None
        '''
        # if tree has no node
        if (node is None):
            result = None
        # traverse the left child recursively
        if (node.has_left()):
            result = self.in_order_(node.get_left(), result)
        
        #base case
        result = result + ' ' + str(node.get_data())
        
        #traverse the right child recursively
        if (node.has_right()):
            result = self.in_order_(node.get_right(), result)
        
        # return the result
        return result.strip()

        
    def pre_order(self, node):
        '''(BTree, BTNode) -> NoneType
        visits all the nodes in the tree by pre-order traversal method.
        REQ: node is not None
        '''
        # you need to take care of the situation where the tree is empty
        # see in_order_
        print(node.get_data(), " ", end="")
        if (node.has_left()):
            self.pre_order(node.get_left())
        if(node.has_right()):
            self.pre_order(node.get_right())

    def post_order(self, node):
        '''(BTree, BTNode) -> NoneType
        visits all the nodes in the tree by post-order traversal method.
        '''
        # you need to take care of the situation where the tree is empty 
        # see in_order_
        if (node.has_left()):
            self.post_order(node.get_left())
        if(node.has_right()):
            self.post_order(node.get_right())
        print(node.get_data(), " ", end="")
        
    def depth(self, node):
        '''(BTree, BTNode) -> int
        returns the depth of a node in this tree 
        '''
        #base case
        # based on the definition, a tree is either a pointer to None or...
        # so we have to check if node is None
        if (node is None or node.is_root()):
            result = 0
        else:
            result = 1 + self.depth(node.get_parent())
        return result
       
    def height(self, node):
        '''(BTree, BTNode) -> int
        returns the height of this tree '''
        #base case
        # based on the definition, a tree is either a pointer to None or...
        # so we have to check if node is None
        if (node is None or node.is_leaf()):
            result = 0
        else:
            result = 1 + max(self.height(node.get_right()), self.height(node.get_left()))
        return result
        
if (__name__ == "__main__"):
    ''' create this BT 
                 A
               /   \
             B      C   
            /\       \
           D  E      F
                    /
                   G
    '''
    
    root = BTNode("A")
    btree = BTree(root)
    node_B = btree.add_left(btree.get_root(), "B")
    node_C = btree.add_right(btree.get_root(), "C")
    node_D = btree.add_left(node_B, "D")
    node_E = btree.add_right(node_B, "E")
    node_F = btree.add_right(node_C, "F")
    node_G = btree.add_left(node_F, "G") 

    btree.pre_order(root)
    print()
    btree.in_order(root)
    print()
    btree.post_order(root)
    print()

    print("depth = ", btree.depth(root))
    print("depth = ", btree.depth(node_G))
    print("Height = ", btree.height(root))
    print(btree.in_order_(root))
    
    