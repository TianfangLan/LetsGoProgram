class BTNode(object):
    """A node in a binary tree."""

    def __init__(self, value, left=None, right=None):
        """(BTNode, int, BTNode, BTNode) -> NoneType
        Initialize this node to store value and have children left and right,
        as well as depth 0.
        """
        self.value = value
        self.left = left
        self.right = right
        self.d = 0

    def __str__(self):
        return self._str_helper("")

    def _str_helper(self, indentation=""):
        """(BTNode, str) -> str
        Return a "sideways" representation of the subtree rooted at this node,
        with right subtrees above parents above left subtrees and each node on
        its own line, preceded by as many TAB characters as the node's depth.
        """
        ret = ""

        if(self.right is not None):
            ret += self.right._str_helper(indentation + "\t") + "\n"
        ret += indentation + str(self.value) + "\n"
        if(self.left is not None):
            ret += self.left._str_helper(indentation + "\t") + "\n"
        return ret

    def set_depth(self, depth):
        '''(BTNode, int) -> Nonetype
        the method will set the d parameter of all nodes in the tree rooted
        at a particular node, starting at the provided value.
        REQ: the depth should be a int
        '''
        self.d = depth
        if (self.left is not None):
            self.left.set_depth(depth + 1)
        if (self.right is not None):
            self.right.set_depth(depth + 1)

    def leaves_and_internals(self):
        ''' (BTNode) -> tuple of 2 sets
        the method will return a tuple with 2 sets, the first one is the set
        of all values stored in the leaves of the tree. The second one is the
        values stored in the internal nodes of the tree. The root is neither
        leaves nor internals.
        '''
        result = (set(), set())
        if (self.left is not None or self.right is not None):
            result = self.include_root_helper()
            result[1].remove(self.value)
        return result

    def include_root_helper(self):
        ''' (BTNode) -> tuple of 2 sets
        the method will return a tuple with 2 sets, the first one is the set
        of all values stored in the leaves of the tree. The second one is the
        values stored in the internal nodes of the tree. However, this
        method will count root as a internal or leaves.
        '''
        leaves = set()
        internals = set()
        children = [self.left, self.right]
        if (self.left is None and self.right is None):
            leaves.add(self.value)
        else:
            internals.add(self.value)
            for child in children:
                if child is not None:
                    child_tuple = child.include_root_helper()
                    leaves = leaves | child_tuple[0]
                    internals = internals | child_tuple[1]
        return((leaves, internals))

    def sum_to_deepest(self):
        ''' (BTNode) -> int
        the method will return the sum of all values on the path from this node
        to the deepest leaf node, if there are multiple choices, return the
        largest one.
        '''
        list_bra = self.helper(0)
        re_list = []
        position = 0
        for depth in list_bra[1]:
            if depth == max(list_bra[1]):
                re_list.append(list_bra[0][position])
            position += 1
        return max(re_list)

    def helper(self, depth):
        ''' (BTNode, int) -> tuple
        the method will return the sum of all values on the path from this node
        to the deepest leaf node, if there are multiple choices, return the
        largest one.
        '''
        children = [self.left, self.right]
        sumlist = []
        depthlist = []
        if (self.left is None and self.right is None):
            sumlist.append(self.value)
            depthlist.append(depth)
        for child in children:
            if (child is not None):
                next1 = child.helper(depth + 1)
                for sums in next1[0]:
                    sumlist.append(self.value + sums)
                for dep in next1[1]:
                    depthlist.append(dep)
        return (sumlist, depthlist)
