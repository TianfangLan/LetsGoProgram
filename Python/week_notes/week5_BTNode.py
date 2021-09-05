class TNode():
    ''' a class that represents a binary tree node'''
    def __init__(self, data, left_child=None, right_child=None):
        '''(TNode,obj, TNode,  TNode) -> NoneType
        Constructs a binary tree nodes with the given data'''
        
        self._left = left_child
        self._data = data
        self._right = right_child

    def set_left(self, left_child):
        '''(TNode, TNode) -> NoneType
        set the left child to the given node'''
        self._left = left_child

    def set_right(self, right_child):
        '''(TNode, TNode) -> NoneType
        set the right child to the given node'''
        self._right = right_child
    def set_data(self, data):
        '''(TNode, obj) -> NoneType
        set the data at this node to the given data'''
        self._data = data    
    
    def get_left(self):
        '''(TNode) -> TNode
        return the pointer to the left child'''
        return self._left

    def get_right(self):
        '''(TNode) -> TNode
        return the pointer to the right child'''
        return self._right   
    def get_data(self):
        '''(TNode) -> obj
        return the data stored in this node'''
        return self._data


# A node to better represent a Binary Tree Node
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
    
if (__name__ == "__main__"):
    ''' create this BT using TNode
                 A
               /   \
             B      C   
            /\       \
           D  E      F
                    /
                   G
    '''
    node_G = TNode("G")
    node_F = TNode("F", node_G)
    node_C = TNode("C", None, node_F)
    node_D = TNode("D")
    node_E = TNode("E")
    node_B = TNode("B",node_D, node_E)
    node_A = TNode("A",node_B, node_C)
    
    print("Node B's pointer contains: " + str(hex(id(node_B))))
    print("Left and right children of B are at:" + str(hex(id(node_D))) +" and " +str(hex(id(node_E))))
    print("Left and right children of B are at:" + str(hex(id(node_B.get_left()))) +" and " +str(hex(id(node_B.get_right()))))
    
    # An alternative way of creating this tree
    bt = TNode ("A",TNode("B",TNode("D"), TNode("E")) 
                    ,TNode("C", None, TNode("F", TNode("G"))))    
    print("Node B's pointer contains: " + str(hex(id(bt.get_left()))))
    print("Left and right children of B are at:" + 
          str(hex(id(bt.get_left().get_left()))) +" " +
          str(hex(id(bt.get_left().get_right()))))
    
    print("\n")
    ''' create this BT using BTNode
                 A
               /   \
             B      C   
            /\       \
           D  E      F
                    /
                   G
    '''
    node_G = BTNode("G")
    node_F = BTNode("F", None,node_G)
    node_G.set_parent(node_F)
    node_C = BTNode("C", None, None, node_F)
    node_F.set_parent(node_C)
    node_D = BTNode("D")
    node_E = BTNode("E")
    node_B = BTNode("B",None, node_D, node_E)
    node_D.set_parent(node_B)
    node_E.set_parent(node_B)
    node_A = BTNode("A",None, node_B, node_C)
    node_B.set_parent(node_A)
    print("Node B's parent: " + str(hex(id(node_B.get_parent()))) + " which is the same as A at: " + str(hex(id(node_A))))
    print("Left and right children of B are at:" + str(hex(id(node_D))) +" and " +str(hex(id(node_E))))
    print("Left and right children of B are at:" + str(hex(id(node_B.get_left()))) +" and " +str(hex(id(node_B.get_right()))))
    
    print(node_B.is_left())
    print(node_B.is_right())
    print(node_B.has_left())
    print(node_B.has_right())
    print(node_B.is_root())
    print(node_A.is_root())
    
    
