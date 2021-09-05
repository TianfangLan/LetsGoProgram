from week9_Tree_traversal import BTNode, BTree

class BST(BTree):
    '''representsa BST'''
    def __init__(self, root):
        '''(BST, BTNode) ->NoneType
        constructs a BST by its root'''
        self._root = root
        

    def search(self, node, data):
        '''(BST,BTNode, obj) -> bool 
        return true if the tree contains the given data 
        '''
        # first base case if node is not found
        if(node is None):
            result = False
        # second base case if node is found
        elif(node.get_data() == data):
            result = True
        # reursive case go to left
        elif (data < node.get_data()):
            result = self.search(node.get_left(), data)
        #recursive case go to right
        else:
            result = self.search(node.get_right(), data)
        return result

    def find(self, node, data):
        '''(BST,BTNode, obj) -> BTNode 
        similar to bst_search except that it returns the pointer to the node that 
        contains the data. If data was not found returns None'''
        
        # first base case if node is not found
        if(node is None):
            result = None
        # second base case if node is found
        elif(node.get_data() == data):
            result = node
        # reursive case go to left
        elif (data < node.get_data()):
            result = self.find(node.get_left(), data)
        #recursive case go to right
        else:
            result = self.find(node.get_right(), data)
        return result
        
    def insert(self, node, new_node):
        '''(BST,BTNode, BTNode) -> None
        insert the new_node in the right place
        '''
        # base case 1: This is the first node that is added to the BST
        if(node is None):
            node = new_node 
        
        elif (new_node.get_data() < node.get_data()):
            # base case 2: new_node's data < node'data and node has no left child
            if (not node.has_left()):
                node.set_left(new_node)
                new_node.set_parent(node)
            # recursive case: new_node's data < node's data: go to left
            else:
                self.insert(node.get_left(), new_node)
        else:
            # base case 3: new_node's data >= node's data and node has no right child
            if(not node.has_right()):
                node.set_right(new_node)
                new_node.set_parent(node) 
            # recursive case: new_node's data >= node's data: go to right           
            else:
                self.insert(node.get_right(), new_node)
                          
    
                      
                      
if (__name__ == "__main__"):
    ''' create this BT 
                     40
                   /   \
                 10      70   
                /\       \
               5  20      80
                        /
                       75
    '''
    root = BTNode(40)
    btree = BST(root)
    btree.insert(root, BTNode(10))
    btree.insert(root, BTNode(70))
    btree.insert(root, BTNode(5))
    btree.insert(root, BTNode(20))
    btree.insert(root, BTNode(80))
    btree.insert(root, BTNode(75))
    
    print(btree.in_order_(root))
        
    print(btree.search(root, 70))
    print(btree.search(root, 3))
    print(btree.find(root, 3))

