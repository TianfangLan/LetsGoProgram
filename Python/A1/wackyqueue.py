"""
# Copyright Nick Cheng, 2018
# Distributed under the terms of the GNU General Public License.
#
# This is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This file is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this file.  If not, see <http://www.gnu.org/licenses/>.

# Tianfang Lan
"""

from wackynode import WackyNode

# Do not add import statements or change the one above.
# Write your WackyQueue class code below.


class WackyQueue():
    '''The class represents a wackyqueue. The wackyqueue contains a sequence
    of objects, each Node has a priority and will be sorted from higer priority
    to lower priority.'''
    def __init__(self):
        '''(WackyQueue) -> Nonetype
        Initializes the reference for a new WackyQueue'''
        # set the first items in two link lists to be None at the beginning
        # heado is for the odd link list
        self._heado = None
        # heade is for the even link list
        self._heade = None

    def insert(self, obj, pri):
        '''(WackyQueue, obj, int) -> Nonetype
        This method is for inserting a new WackNode into the WackyQueue,
        WackNodes will be sorted from high priority to low priority
        '''
        # create the wackynode, obj is the item, pri is the priority
        Node = WackyNode(obj, pri)
        # insert is a boolean shows whether the Node is inserted or not
        insert = False
        # The following steps are setting the heads for even and odd link lists
        # if there is no item in the queue, the node will be the head of odd ll
        if ((self._heado is None) and (self._heade is None)):
            self._heado = Node
            insert = True
        # set another head if the even head is None
        # if the input priority is larger than the odd head's priority
        # then the current odd head will be the even head
        # following case is to set the new Odd head
        elif ((self._heado is not None) and
              (pri > self._heado.get_priority())):
            # let the Node point to the current even link list
            Node.set_next(self._heade)
            # swap the whole odd link list to be the even link list
            self._heade = self._heado
            # set the Node to be the new head of the odd link list and swap
            # the odd even link list to be the new odd link list
            self._heado = Node
            insert = True
        # if it is smaller or equal, it will be the head of the even link list
        elif ((self._heado is not None) and
              (self._heade is None) and
              (pri <= self._heado.get_priority())):
            self._heade = Node
            insert = True
        # following case is to set the even head
        # when both heads are already exist
        elif ((self._heado is not None) and
              (self._heade is not None) and
              (self._heado.get_priority() >= pri and
              pri > self._heade.get_priority())):
            # set the current odd link list after the head
            next_odd = self._heado.get_next()
            # set the current even link list
            next_even = self._heade
            # the new node will lead the current odd link list to be the new
            # even link list
            Node.set_next(next_odd)
            # the new node will be the new head of even link list
            self._heade = Node
            # let the old even link list follow the odd head
            # it becomes to the new odd link list
            self._heado.set_next(next_even)
            insert = True
        # the changing head cases are all done!!!
        # create current Node in odd and even link list
        curr_odd = self._heado
        curr_even = self._heade
        # get the priority of the odd and even nodes
        pri_odd = self._heado.get_priority()
        if (curr_even is not None):
            pri_even = self._heade.get_priority()
        else:
            pri_even = None
        # set size of the two link lists
        size1 = 1
        size2 = 1
        # get the two priorites of nodes in odd link list
        # one is just larger then the insert pri the other is just less then it
        while (not insert and curr_odd is not None and pri_odd >= pri):
            # set a previous node
            prev_odd = curr_odd
            curr_odd = curr_odd.get_next()
            if (curr_odd is not None):
                pri_odd = curr_odd.get_priority()
            else:
                pri_odd = None
            # set the previous node priority
            prev_pri_odd = prev_odd.get_priority()
            size2 += 1
        # get the two priorites of nodes in even link list
        # one is just larger then the insert pri the other is just less then it
        while (not insert and curr_even is not None and pri_even >= pri):
            prev_even = curr_even
            curr_even = curr_even.get_next()
            if (curr_even is not None):
                pri_even = curr_even.get_priority()
            else:
                pri_even = None
            # set the previous node priority
            prev_pri_even = prev_even.get_priority()
            size1 += 1
        # the following starts to judge where shoulde the new node be inserted
        # this case is a very special case when insert priority is the smallest
        # and the last priorities in odd and even lists are the same
        if (not insert and pri_even is None and pri_odd is None and
           (size1 == size2)):
            prev_odd.set_next(Node)
        elif (not insert and pri_even is None and pri_odd is None and
              (size1 < size2)):
            prev_even.set_next(Node)
        # this is the case of the new node will be inserted right after the
        # node from even list and just before the node in the odd node list
        elif (not insert and prev_pri_odd >= prev_pri_even and
              (pri_even is None or pri_odd >= pri_even)):
            # first off insert the new node into the odd list, and new node
            # should bring the after even list to the odd list
            # let the new node point to the current even after list
            Node.set_next(curr_even)
            # let the previous odd point to new Node
            prev_odd.set_next(Node)
            # then the neweven list should be filled with
            # even front and odd after
            prev_even.set_next(curr_odd)
        # the following case is the new node be inserted just after the
        # node from odd list and right before the node in the even node list
        elif (not insert and prev_pri_odd <= prev_pri_even and
              (pri_odd is None or pri_odd <= pri_even)):
            # after the odd node, the new node will be in the even link list
            # let the new node point to the current odd list
            Node.set_next(curr_odd)
            # make the new node get into the even list
            prev_even.set_next(Node)
            # make the front odd link list point to the after even link list
            prev_odd.set_next(curr_even)

    def isempty(self):
        ''' (WackyQueue) -> bool
        the method returns a boolean represents whether the queue is empty or
        not
        '''
        return (self._heado is None)

    def extracthigh(self):
        ''' (WackyQueue) -> obj
        the method will return the first item in the WackyQueue and delete it
        from the queue.'''
        result = None
        if (not self.isempty()):
            result = self._heado.get_item()
            # store the data of even link list
            odd_ll = self._heado.get_next()
            # let the old head point to nowhere
            self._heado.set_next(None)
            # delete the first item and swap 2 link lists
            self._heado = self._heade
            self._heade = odd_ll
        return result

    def changepriority(self, obj, pri):
        '''(WackyQueue, obj, int) -> Nonetype
        the method will change the priority of the first copy of object obj to
        pri. If the priority is changed, the insert time will also been refresh
        '''
        # set a boolean represent the node has been changed or not
        changed = False
        # set current odd and current even Nodes
        curr_odd = self._heado
        curr_even = self._heade
        if (self._heado is None):
            pass
        elif (curr_odd.get_item() == obj):
            # use the extracthigh to lose the first item
            self.extracthigh()
            # insert the item with the new priority back
            self.insert(obj, pri)
        elif (self._heado.get_item() != obj and self._heade is None):
            pass
        # the following case is when the object is the head of the
        # even link list
        elif (curr_even.get_item() == obj):
            # get the node after the head of the even list
            even_ll = self._heade.get_next()
            # let the head of even list point to nowhere
            self._heade.set_next(None)
            # swap the odd and even link list
            self._heade = self._heado.get_next()
            self._heado.set_next(even_ll)
            # insert the item with the new priority back
            self.insert(obj, pri)
        else:
            # keep doing when the list is not full looped
            # the object is not found in the list
            while (not changed and
                   (curr_odd is not None or curr_even is not None) and
                   obj != curr_odd.get_item() and
                   (curr_even is None or obj != curr_even.get_item())):
                prev_even = curr_even
                # because the entered curr_even might be none when it comes to
                # the odd the last item is from odd list
                if (curr_even is not None):
                    curr_even = curr_even.get_next()
                else:
                    curr_even = None
                prev_odd = curr_odd
                curr_odd = curr_odd.get_next()
                if (curr_odd is not None and curr_odd.get_item() == obj):
                    # if this case is used, the priority has been changed
                    changed = True
                    # swap the odd and even link list
                    prev_odd.set_next(curr_even)
                    after_even = curr_odd.get_next()
                    prev_even.set_next(after_even)
                    # delete the certain Node
                    curr_odd.set_next(None)
                    # insert the Node with priority changed
                    self.insert(obj, pri)
                elif (curr_even is not None and not changed and
                      curr_even.get_item() == obj):
                    # swap the odd and even link list
                    prev_even.set_next(curr_odd.get_next())
                    after_odd = curr_even.get_next()
                    curr_odd.set_next(after_odd)
                    # delete the certain Node
                    curr_even.set_next(None)
                    # insert the Node with priority changed
                    self.insert(obj, pri)

    def negateall(self):
        '''(WackyQueue) -> Nonetype
        this method will negative priorities of all objects in the WackyQueue,
        The insertion time is changed in this method, so the Node with same
        priority will be reversed.'''
        if (not self.isempty() and self._heade is None):
            # the new priority should be negate
            new_pri = -1 * self._heado.get_priority()
            # set the new priority to the head of the odd link list
            self._heado.set_priority(new_pri)
        elif (not self.isempty()):
            # set a size to count the size of the link list
            size = 0
            # set the current odd and even node to be head of the nodes
            curr_odd = self._heado
            curr_even = self._heade
            # set the prev of the current Node to be None
            prev_odd = None
            prev_even = None
            # keep changing the Node with positive priority
            while (curr_even is not None or curr_odd is not None):
                # when curr is not the last node of the certain link list
                if (curr_even is not None):
                    # get the priority of the node
                    even_pri = -1 * curr_even.get_priority()
                    # reset the priority of the node
                    curr_even.set_priority(even_pri)
                    # first store the next node of current
                    next_even = curr_even.get_next()
                    # reverse the position of two
                    curr_even.set_next(prev_even)
                    size += 1
                    prev_even = curr_even
                    curr_even = next_even
                # same as the case of even
                if (curr_odd is not None):
                    # get the priority of the node
                    odd_pri = -1 * curr_odd.get_priority()
                    # reset the priority of the node
                    curr_odd.set_priority(odd_pri)
                    # first store the next node of current
                    next_odd = curr_odd.get_next()
                    # reverse the position of two
                    curr_odd.set_next(prev_odd)
                    size += 1
                    prev_odd = curr_odd
                    curr_odd = next_odd
            # we have reversed both of the link lists
            # if the size of the link list is a odd number
            # we do not have to swap the 2 lists
            if (size % 2 == 1):
                self._heado = prev_odd
                self._heade = prev_even
            # if the size is a even number
            # we have to swap 2 lists
            else:
                self._heado = prev_even
                self._heade = prev_odd

    def getoddlist(self):
        '''(WackyQueue) -> WackyNode
        this method will return a pointer point to the link list with the
        first object, the third object, the fifth object...
        '''
        return self._heado

    def getevenlist(self):
        '''(WackyQueue) -> WackyNode
        this method will return a pointer point to the link list with the
        second object, the fourth object, the sixth object...'''
        return self._heade
