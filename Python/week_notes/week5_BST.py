from week5_BTNode import *
from week5_BT import *
from week2_Container import Queue
# improve this code by creating a class for BST
# this class should extend class BTree (i.e. BST should inherits from BTree)
# The following functions therefore will be BST's methods.
class BST():
    '''representsa BST'''
    def __init__(self, root):
        '''(BST, BTNode) ->NoneType
        constructs a BST by its root'''
        self._root = root
        

    def search(self, data):
        '''(BST,obj) -> bool 
        return true if the tree contains the given data 
        '''
        
        # start fron the root
        cur = self._root
        # traverse the tree
        while (cur is not None and cur.get_data() != data):
            # traverse the left path if data is less than current pointer's data
            if (data < cur.get_data()):
                cur = cur.get_left()
            # otherwise go right
            else:
                cur = cur.get_right()
        # return (if cur is none you haven't found it, so return false otherwise true)
        return cur != None

    def find(self, data):
        '''(BST,obj) -> BTNode 
        similar to bst_search except that it returns the pointer to the node that 
        contains the data. If data was not found returns None'''
        
        # start fron the root
        cur = self._root
        # traverse the tree
        while (cur is not None and cur.get_data() != data):
            # traverse the left path if data is less than current pointer's data
            if (data < cur.get_data()):
                cur = cur.get_left()
            # otherwise go right
            else:
                cur = cur.get_right()
        # return cur pointer        
        return cur 

    def insert(self, data):
        '''(BST,obj) -> None
        create a node containing data and insert it in a right place
        '''
        #create a BTNode from the given data
        node = BTNode(data)
        # start fron the root
        cur = self._root
        # traverse the tree
        while (cur is not None):
            # keep the pointer to parent node before moving down
            parent = cur
            # traverse the left path if data is less than current pointer's data
            if (data < cur.get_data()):
                cur = cur.get_left()
            # otherwise take the right route
            else:
                cur = cur.get_right()
        #check the data in parent node to determine which child (left or right) should be added
        # so added as a right child if data < parent's data
        if (data < parent.get_data()):
            # establish the double link between parent and child
            parent.set_left(node)
            node.set_parent(parent)
        # otherwise it should be a right child
        else:
            parent.set_right(node)
            node.set_parent(parent)
    
    def delete(self, data):
        ''' (BST,Obj) -> NoneType
        Delete the node, whose data is given, if it exists
        if such a node does not exists, the BST remains unchanged
        '''
        # find to-be-deleted node [find(data)]
        deleted_node = self.find(data)
        # if such a node exists 
        if (deleted_node is not None):
            #if the to-be-deleted node has no children 
            if (not (deleted_node.has_right() or deleted_node.has_left())): 
                # if the deleted node is its parent's left child
                if (deleted_node.is_left()):
                    # set the left child of the parent to None
                    deleted_node.get_parent().set_left(None)
                #else (it is a right child)
                else:
                    #set the right child of the parent to None
                    deleted_node.get_parent().set_right(None)
                #Nulify the deleted node
                deleted_node.set_parent(None)      
            #if the to-be-deleted node has one child
            elif ((deleted_node.has_left() and (not deleted_node.has_right())) 
                  or (deleted_node.has_right() and (not deleted_node.has_left()))):
                #get its child
                if (deleted_node.has_right()):
                    child = deleted_node.get_right()
                else:
                    child = deleted_node.get_left()
                # if the deleted node is its parent's left child 
                if (deleted_node.get_parent().get_left() is deleted_node):
                    # let its child to be its parents left child
                    deleted_node.get_parent().set_left(child)
                    # new child should poitn to its new parent
                    child.set_parent(deleted_node.get_parent())
                #else (the deleted node is right child of its parent
                else:
                    # let its child to be its parents right child
                    deleted_node.get_parent().set_right(child)
                    # new child should poitn to its new parent
                    child.set_parent(deleted_node.get_parent())
                #Nulify the deleted node 
                deleted_node.set_parent(None) 
                deleted_node.set_left(None)
                deleted_node.set_right(None)         
            # the to-be-deleted node has two children 
            else: 
                #get its right child and call it successor
                successor = deleted_node.get_right()
                
                #start from successor, go down on left side until left of the
                # sucessor is not None(because left side 
                #contain the next smallest value after the given data) 
                while (successor.get_left() is not None):
                    successor = succdessor.get_left()
                
                # copy the successor data into the deleted_node
                deleted_node.set_data(successor.get_data())
                
                # successor can have only two stauts. it either has no child, or 
                # one RIGHT child. why?
                
                
                #if successor has a right child, 
                if (successor.has_right()):
                    # if successor itself is a right child of its parent
                    if(successor.is_right()):
                        # right child of the successor becomes the right child of successor's parent
                        successor.get_parent().set_right(successor.get_right())
                        # child should point to parent too
                        successor.get_right().set_parent(successor.get_parent())
                    # else if successor itself is a left child of its parent
                    else:
                        # left child of the successor becomes the right child of the successor's parent
                        successor.get_parent().set_left(successor.get_right())
                        # child should point to parent too
                        successor.get_right(set_parent(successor.get_parent()))
                    # successor right should be None
                    successor.set_right(None)
                # else (it has no child, so remove it)
                else:
                    # if successor is a right child
                    if (successor.is_right()):
                        # set its parent right child to None
                        successor.get_parent().set_right(None)
                    # else (it is left child)
                    else:
                        # set its parent left child to None
                        successor.get_parent().set_left(None)
                    # nulify successor's parent
                    successor.set_parent(None)
                        
                    
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
    btree.insert(10)
    btree.insert(70)
    btree.insert(5)
    btree.insert(20)
    btree.insert(80)
    btree.insert(75)
    
    print(btree.BFS())
        
    print(btree.search(70), hex(id(btree.find(70))))
    print(btree.search(3), hex(id(btree.find(3))))

    btree.delete(70)
    print(btree.BFS())
