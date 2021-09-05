from week5_BTNode import *
from week2_Container import Queue

# complete this code by adding exception where it needs to

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
    # for now we cannot remvove nodes unless we define an strategy for replacing a node when it has two children e.g. deciding on replacing it with its left or right child. If the removed node is either an external node or has only one child, the solution is straight forward.
    def BFS(self):
        '''(BTree) -> str
        traverse the tree in Breadth First search mehtod
        '''
        # create an empty string to hold tree's data
        result = ""
        #add the root to a qeueue
        queue = Queue()
        queue.put(self._root)
        #While queue is not empty
        while (not queue.is_empty()):
            # remove the node form the queue
            node = queue.get()
            # and insert its left and right child to the queue
            if (node.has_left()):
                queue.put(node.get_left())
            if (node.has_right()):
                queue.put(node.get_right())
            # add the data stored in the node to the reuslt
            result = result + " " + str(node.get_data())
        # return the result
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
    
    print(btree.BFS())
    
    
    
