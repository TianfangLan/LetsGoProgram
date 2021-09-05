import unittest
import random
# import hijack
import wackyqueue as a1


def split_source(src_list, negate=False):
    target_list = src_list[:]
    if negate:
        target_list = list(map(lambda pair: (pair[0], pair[1] * -1), target_list))
    else:
        target_list.reverse()
    odd = sorted(target_list[::2], key=lambda pair: pair[1], reverse=True)
    even = sorted(target_list[1::2], key=lambda pair: pair[1], reverse=True)
    return odd, even


def sort_list(lst1, lst2=None, ordered=True, descending=False):
    if ordered:
        return sorted(lst1 + (lst2 if lst2 else []), key=lambda pair: pair[1], reverse=descending)
    else:
        return sorted(lst1 + (lst2 if lst2 else []), key=lambda pair: random.random())


def build_solution(soln_list):
    wq = curr_wq = None
    for data, pri in soln_list:
        node = a1.WackyNode(data, pri)
        if not wq:
            wq = curr_wq = node
        else:
            curr_wq._next = node
            curr_wq = curr_wq._next
    return wq


def to_string(head_node):
    if not head_node:
        return None
    else:
        return head_node.__str__()


class _TestWackyQueue(unittest.TestCase):

    def setUp(self):
        self.wq = a1.WackyQueue()

    def build_student_solution(self, entry_list):
        for data, priority in entry_list:
            self.wq.insert(data, priority)


class TestWackyQueueBasic(_TestWackyQueue):

    def test_init(self):
        self.assertIsNotNone(self.wq, 'Failed to initialize a WackyQueue.')

    def test_is_empty(self):
        self.assertTrue(self.wq.isempty(), 'New WackyQueue should be empty.')

    def test_get_odd_list_empty(self):
        self.assertIsNone(self.wq.getoddlist(), 'WackyQueue odd list is empty.')

    def test_get_even_list_empty(self):
        self.assertIsNone(self.wq.getevenlist(), 'WackyQueue even list is empty.')

    def test_get_odd_list_non_empty(self):
        src_list = [('hello', 20)]
        self.build_student_solution(src_list)
        self.assertIsNotNone(self.wq.getoddlist(), 'WackyQueue odd list is not empty.')

    def test_get_even_list_non_empty(self):
        src_list = [('world', 10), ('hello', 20)]
        self.build_student_solution(src_list)
        self.assertIsNotNone(self.wq.getevenlist(), 'WackyQueue even list is not empty.')


class TestInsert(_TestWackyQueue):

    def test_insert_1_node(self):
        # insert node
        src_list = [('a48a1', 10)]
        self.build_student_solution(src_list)
        actual_odd = self.wq.getoddlist()
        actual_even = self.wq.getevenlist()

        odd, even = split_source(src_list)
        expect_odd = build_solution(odd)
        expect_even = build_solution(even)

        self.assertEqual(to_string(expect_odd), to_string(actual_odd),
                         'Failed to insert 1 node. Odd node list has incorrect data or incorrect priority.')
        self.assertEqual(to_string(expect_even), to_string(actual_even),
                         'Failed to insert 1 node. Even node list has incorrect data or incorrect priority.')

    def test_insert_3_nodes_ascending_priority(self):
        # insert node
        src_list = [('ex0', 10), ('ex1', 15), ('ex2', 20)]
        self.build_student_solution(src_list)
        actual_odd = self.wq.getoddlist()
        actual_even = self.wq.getevenlist()

        odd, even = split_source(src_list)
        expect_odd = build_solution(odd)
        expect_even = build_solution(even)

        self.assertEqual(to_string(expect_odd), to_string(actual_odd),
                         'Failed to insert 3 nodes in ascending priority order. Odd node list has incorrect data or incorrect priority.')
        self.assertEqual(to_string(expect_even), to_string(actual_even),
                         'Failed to insert 3 nodes in ascending priority order. Even node list has incorrect data or incorrect priority.')

    def test_insert_3_nodes_descending_priority(self):
        # insert node
        src_list = [('ex0', 10), ('ex1', 15), ('ex2', 20)]
        self.build_student_solution(sort_list(src_list, descending=True))
        actual_odd = self.wq.getoddlist()
        actual_even = self.wq.getevenlist()

        odd, even = split_source(src_list)
        expect_odd = build_solution(odd)
        expect_even = build_solution(even)

        self.assertEqual(to_string(expect_odd), to_string(actual_odd),
                         'Failed to insert 3 nodes in descending priority order. Odd node list has incorrect data or incorrect priority.')
        self.assertEqual(to_string(expect_even), to_string(actual_even),
                         'Failed to insert 3 nodes in descending priority order. Even node list has incorrect data or incorrect priority.')

    def test_insert_to_odd_list_exists(self):
        # init
        src_list = [('ex0', 10), ('ex1', 15), ('ex2', 20), ('ex3', 25), ('ex4', 30)]
        self.build_student_solution(src_list)
        # insert node
        inserted = [('insert', 23)]
        self.build_student_solution(inserted)
        actual_odd = self.wq.getoddlist()
        actual_even = self.wq.getevenlist()

        odd, even = split_source(sort_list(src_list, inserted))
        expect_odd = build_solution(odd)
        expect_even = build_solution(even)

        self.assertEqual(to_string(expect_odd), to_string(actual_odd),
                         'Failed to insert to odd list. Odd node list has incorrect data or incorrect priority.')
        self.assertEqual(to_string(expect_even), to_string(actual_even),
                         'Failed to insert to odd list. Even node list has incorrect data or incorrect priority.')

    def test_insert_to_even_list_exists(self):
        # init
        src_list = [('ex0', 10), ('ex1', 15), ('ex2', 20), ('ex3', 25), ('ex4', 30)]
        self.build_student_solution(src_list)
        # insert node
        inserted = [('insert', 18)]
        self.build_student_solution(inserted)
        actual_odd = self.wq.getoddlist()
        actual_even = self.wq.getevenlist()

        odd, even = split_source(sort_list(src_list, inserted))
        expect_odd = build_solution(odd)
        expect_even = build_solution(even)

        self.assertEqual(to_string(expect_odd), to_string(actual_odd),
                         'Failed to insert to even list. Odd node list has incorrect data or incorrect priority.')
        self.assertEqual(to_string(expect_even), to_string(actual_even),
                         'Failed to insert to even list. Even node list has incorrect data or incorrect priority.')

    def test_insert_to_odd_end_list_exists(self):
        # init
        src_list = [('ex0', 10), ('ex1', 15), ('ex2', 20), ('ex3', 25)]
        self.build_student_solution(src_list)
        # insert node
        inserted = [('insert', 5)]
        self.build_student_solution(inserted)
        actual_odd = self.wq.getoddlist()
        actual_even = self.wq.getevenlist()

        odd, even = split_source(sort_list(src_list, inserted))
        expect_odd = build_solution(odd)
        expect_even = build_solution(even)

        self.assertEqual(to_string(expect_odd), to_string(actual_odd),
                         'Failed to insert to end of odd list. Odd node list has incorrect data or incorrect priority.')
        self.assertEqual(to_string(expect_even), to_string(actual_even),
                         'Failed to insert to end of odd list. Even node list has incorrect data or incorrect priority.')

    def test_insert_to_even_end_list_exists(self):
        # init
        src_list = [('ex0', 10), ('ex1', 15), ('ex2', 20), ('ex3', 25), ('ex4', 30)]
        self.build_student_solution(src_list)
        # insert node
        inserted = [('insert', 5)]
        self.build_student_solution(inserted)
        actual_odd = self.wq.getoddlist()
        actual_even = self.wq.getevenlist()

        odd, even = split_source(sort_list(src_list, inserted))
        expect_odd = build_solution(odd)
        expect_even = build_solution(even)

        self.assertEqual(to_string(expect_odd), to_string(actual_odd),
                         'Failed to insert to end of even list. Odd node list has incorrect data or incorrect priority.')
        self.assertEqual(to_string(expect_even), to_string(actual_even),
                         'Failed to insert to end of even list. Even node list has incorrect data or incorrect priority.')

    def test_insert_None_object_to_odd_list_exists(self):
        # init
        src_list = [('ex0', 10), ('ex1', 15), ('ex2', 20), ('ex3', 25), ('ex4', 30)]
        self.build_student_solution(src_list)
        # insert node
        inserted = [(None, 23)]
        self.build_student_solution(inserted)
        actual_odd = self.wq.getoddlist()
        actual_even = self.wq.getevenlist()

        odd, even = split_source(sort_list(src_list, inserted))
        expect_odd = build_solution(odd)
        expect_even = build_solution(even)

        self.assertEqual(to_string(expect_odd), to_string(actual_odd),
                         'Failed to insert data None to odd list. Odd node list has incorrect data or incorrect priority.')
        self.assertEqual(to_string(expect_even), to_string(actual_even),
                         'Failed to insert data None to odd list. Even node list has incorrect data or incorrect priority.')

    def test_insert_None_object_to_even_list_exists(self):
        # init
        src_list = [('ex0', 10), ('ex1', 15), ('ex2', 20), ('ex3', 25), ('ex4', 30)]
        self.build_student_solution(src_list)
        # insert node
        inserted = [(None, 18)]
        self.build_student_solution(inserted)
        actual_odd = self.wq.getoddlist()
        actual_even = self.wq.getevenlist()

        odd, even = split_source(sort_list(src_list, inserted))
        expect_odd = build_solution(odd)
        expect_even = build_solution(even)

        self.assertEqual(to_string(expect_odd), to_string(actual_odd),
                         'Failed to insert data None to even list. Odd node list has incorrect data or incorrect priority.')
        self.assertEqual(to_string(expect_even), to_string(actual_even),
                         'Failed to insert data None to even list. Even node list has incorrect data or incorrect priority.')

    def test_insert_None_object_to_odd_head(self):
        # init
        src_list = [('ex0', 10), ('ex1', 15), ('ex2', 20), ('ex3', 25), ('ex4', 30)]
        self.build_student_solution(src_list)
        # insert node
        inserted = [(None, 50)]
        self.build_student_solution(inserted)
        actual_odd = self.wq.getoddlist()
        actual_even = self.wq.getevenlist()

        odd, even = split_source(sort_list(src_list, inserted))
        expect_odd = build_solution(odd)
        expect_even = build_solution(even)

        self.assertEqual(to_string(expect_odd), to_string(actual_odd),
                         'Failed to insert data None to odd list head. Odd node list has incorrect data or incorrect priority.')
        self.assertEqual(to_string(expect_even), to_string(actual_even),
                         'Failed to insert data None to odd list head. Even node list has incorrect data or incorrect priority.')

    def test_insert_None_object_to_even_head(self):
        # init
        src_list = [('ex0', 10), ('ex1', 15), ('ex2', 20), ('ex3', 25), ('ex4', 30)]
        self.build_student_solution(src_list)
        # insert node
        inserted = [(None, 28)]
        self.build_student_solution(inserted)
        actual_odd = self.wq.getoddlist()
        actual_even = self.wq.getevenlist()

        odd, even = split_source(sort_list(src_list, inserted))
        expect_odd = build_solution(odd)
        expect_even = build_solution(even)

        self.assertEqual(to_string(expect_odd), to_string(actual_odd),
                         'Failed to insert data None to even list head. Odd node list has incorrect data or incorrect priority.')
        self.assertEqual(to_string(expect_even), to_string(actual_even),
                         'Failed to insert data None to even list head. Even node list has incorrect data or incorrect priority.')

    def test_insert_equal_priority_use_odd_head_priority(self):
        # init
        src_list = [('ex0', 10), ('ex1', 15)]
        self.build_student_solution(src_list)
        # insert node
        inserted = [('insert', 15)]
        self.build_student_solution(inserted)
        actual_odd = self.wq.getoddlist()
        actual_even = self.wq.getevenlist()

        odd, even = split_source([('ex0', 10), ('insert', 15), ('ex1', 15)])  # secondary key sort not implemented
        expect_odd = build_solution(odd)
        expect_even = build_solution(even)

        self.assertEqual(to_string(expect_odd), to_string(actual_odd),
                         'Failed to insert equal priority element. Odd node list has incorrect data or incorrect priority.')
        self.assertEqual(to_string(expect_even), to_string(actual_even),
                         'Failed to insert equal priority element. Even node list has incorrect data or incorrect priority.')

    def test_insert_equal_priority_use_even_head_priority(self):
        # init
        src_list = [('ex0', 10), ('ex1', 15), ('ex2', 20)]
        self.build_student_solution(src_list)
        # insert node
        inserted = [('insert', 15)]
        self.build_student_solution(inserted)
        actual_odd = self.wq.getoddlist()
        actual_even = self.wq.getevenlist()

        odd, even = split_source([('ex0', 10), ('insert', 15), ('ex1', 15), ('ex2', 20)])  # secondary key sort not implemented
        expect_odd = build_solution(odd)
        expect_even = build_solution(even)

        self.assertEqual(to_string(expect_odd), to_string(actual_odd),
                         'Failed to insert equal priority element. Odd node list has incorrect data or incorrect priority.')
        self.assertEqual(to_string(expect_even), to_string(actual_even),
                         'Failed to insert equal priority element. Even node list has incorrect data or incorrect priority.')

    def test_insert_equal_priority_use_odd_body_priority(self):
        # init
        src_list = [('ex0', 10), ('ex1', 15), ('ex2', 20), ('ex3', 25), ('ex4', 30)]
        self.build_student_solution(src_list)
        # insert node
        inserted = [('inserted', 20)]
        self.build_student_solution(inserted)
        actual_odd = self.wq.getoddlist()
        actual_even = self.wq.getevenlist()

        odd, even = split_source([('ex0', 10), ('ex1', 15), ('inserted', 20), ('ex2', 20), ('ex3', 25), ('ex4', 30)])
        expect_odd = build_solution(odd)
        expect_even = build_solution(even)

        self.assertEqual(to_string(expect_odd), to_string(actual_odd),
                         'Failed to insert equal priority element. Odd node list has incorrect data or incorrect priority.')
        self.assertEqual(to_string(expect_even), to_string(actual_even),
                         'Failed to insert equal priority element. Even node list has incorrect data or incorrect priority.')

    def test_insert_equal_priority_use_even_body_priority(self):
        # init
        src_list = [('ex0', 10), ('ex1', 15), ('ex2', 20), ('ex3', 25), ('ex4', 30)]
        self.build_student_solution(src_list)
        # insert node
        inserted = [('inserted', 15)]
        self.build_student_solution(inserted)
        actual_odd = self.wq.getoddlist()
        actual_even = self.wq.getevenlist()

        odd, even = split_source([('ex0', 10), ('inserted', 15), ('ex1', 15), ('ex2', 20), ('ex3', 25), ('ex4', 30)])
        expect_odd = build_solution(odd)
        expect_even = build_solution(even)

        self.assertEqual(to_string(expect_odd), to_string(actual_odd),
                         'Failed to insert equal priority element. Odd node list has incorrect data or incorrect priority.')
        self.assertEqual(to_string(expect_even), to_string(actual_even),
                         'Failed to insert equal priority element. Even node list has incorrect data or incorrect priority.')

    def test_insert_all_negative_priority(self):
        # insert node
        src_list = [('ex0', -10), ('ex1', -15), ('ex2', -20), ('ex3', -25), ('ex4', -30)]
        self.build_student_solution(sort_list(src_list, ordered=False))
        actual_odd = self.wq.getoddlist()
        actual_even = self.wq.getevenlist()

        odd, even = split_source(src_list)
        expect_odd = build_solution(odd)
        expect_even = build_solution(even)

        self.assertEqual(to_string(expect_odd), to_string(actual_odd),
                         'Failed to insert negative priority element. Odd node list has incorrect data or incorrect priority.')
        self.assertEqual(to_string(expect_even), to_string(actual_even),
                         'Failed to insert negative priority element. Even node list has incorrect data or incorrect priority.')

    def test_insert_mixed_priority(self):
        # insert node
        src_list = [(2.333, -22), (False, -6), (('A', 'B'), 0), (True, 11), (None, 30), ('+inf#', float('inf'))]
        self.build_student_solution(sort_list(src_list, ordered=False))
        actual_odd = self.wq.getoddlist()
        actual_even = self.wq.getevenlist()

        odd, even = split_source(src_list)
        expect_odd = build_solution(odd)
        expect_even = build_solution(even)

        self.assertEqual(to_string(expect_odd), to_string(actual_odd),
                         'Failed to insert element. Odd node list has incorrect data or incorrect priority.')
        self.assertEqual(to_string(expect_even), to_string(actual_even),
                         'Failed to insert element. Even node list has incorrect data or incorrect priority.')

    def test_priority_pos_infinity(self):
        # init
        src_list = [('ex0', 10), ('ex1', 15), ('ex2', 20), ('ex3', 25), ('ex4', 30)]
        self.build_student_solution(src_list)
        # insert node
        inserted = [('+inf#', float('inf'))]
        self.build_student_solution(inserted)
        actual_odd = self.wq.getoddlist()
        actual_even = self.wq.getevenlist()

        odd, even = split_source(sort_list(src_list, inserted))
        expect_odd = build_solution(odd)
        expect_even = build_solution(even)

        self.assertEqual(to_string(expect_odd), to_string(actual_odd),
                         'Failed to insert data None to even list. Odd node list has incorrect data or incorrect priority.')
        self.assertEqual(to_string(expect_even), to_string(actual_even),
                         'Failed to insert data None to even list. Even node list has incorrect data or incorrect priority.')

    def test_priority_neg_infinity_odd_tail(self):
        # init
        src_list = [('ex0', 10), ('ex1', 15), ('ex2', 20), ('ex3', 25)]
        self.build_student_solution(src_list)
        # insert node
        inserted = [('-inf#', float('-inf'))]
        self.build_student_solution(inserted)
        actual_odd = self.wq.getoddlist()
        actual_even = self.wq.getevenlist()

        odd, even = split_source(sort_list(src_list, inserted))
        expect_odd = build_solution(odd)
        expect_even = build_solution(even)

        self.assertEqual(to_string(expect_odd), to_string(actual_odd),
                         'Failed to insert data None to odd list tail. Odd node list has incorrect data or incorrect priority.')
        self.assertEqual(to_string(expect_even), to_string(actual_even),
                         'Failed to insert data None to odd list tail. Even node list has incorrect data or incorrect priority.')

    def test_priority_neg_infinity_even_tail(self):
        # init
        src_list = [('ex0', 10), ('ex1', 15), ('ex2', 20), ('ex3', 25), ('ex4', 30)]
        self.build_student_solution(src_list)
        # insert node
        inserted = [('-inf#', float('-inf'))]
        self.build_student_solution(inserted)
        actual_odd = self.wq.getoddlist()
        actual_even = self.wq.getevenlist()

        odd, even = split_source(sort_list(src_list, inserted))
        expect_odd = build_solution(odd)
        expect_even = build_solution(even)

        self.assertEqual(to_string(expect_odd), to_string(actual_odd),
                         'Failed to insert data None to even list tail. Odd node list has incorrect data or incorrect priority.')
        self.assertEqual(to_string(expect_even), to_string(actual_even),
                         'Failed to insert data None to even list tail. Even node list has incorrect data or incorrect priority.')


class TestChangePriority(_TestWackyQueue):

    def test_non_existing_object(self):
        src_list = [('ex0', 10), ('ex1', 5)]
        self.build_student_solution(src_list)
        self.wq.changepriority('csca48a1', 100)
        actual_odd = self.wq.getoddlist()
        actual_even = self.wq.getevenlist()

        odd, even = split_source(sort_list(src_list))
        expect_odd = build_solution(odd)
        expect_even = build_solution(even)

        self.assertEqual(to_string(expect_odd), to_string(actual_odd),
                         'Failed to change odd head priority with same priority.')
        self.assertEqual(to_string(expect_even), to_string(actual_even),
                         'Failed to change odd head priority with same priority.')

    def test_change_odd_head_same_priority(self):
        src_list = [('ex0', 10), ('ex1', 5)]
        self.build_student_solution(src_list)
        self.wq.changepriority('ex0', 10)
        actual_odd = self.wq.getoddlist()
        actual_even = self.wq.getevenlist()

        odd, even = split_source(sort_list(src_list))
        expect_odd = build_solution(odd)
        expect_even = build_solution(even)

        self.assertEqual(to_string(expect_odd), to_string(actual_odd),
                         'Failed to change odd head priority with same priority.')
        self.assertEqual(to_string(expect_even), to_string(actual_even),
                         'Failed to change odd head priority with same priority.')

    def test_change_odd_head_higher_priority_remain_odd_head(self):
        src_list = [('ex0', 10), ('ex1', 5)]
        self.build_student_solution(src_list)
        self.wq.changepriority('ex0', 100)
        actual_odd = self.wq.getoddlist()
        actual_even = self.wq.getevenlist()

        src_list = [('ex0', 100), ('ex1', 5)]
        odd, even = split_source(sort_list(src_list))
        expect_odd = build_solution(odd)
        expect_even = build_solution(even)

        self.assertEqual(to_string(expect_odd), to_string(actual_odd),
                         'Failed to change odd head priority with higher priority than original odd head.')
        self.assertEqual(to_string(expect_even), to_string(actual_even),
                         'Failed to change odd head priority with higher priority than original odd head.')

    def test_change_odd_head_lower_priority_to_be_even_head(self):
        src_list = [('ex0', 10), ('ex1', 5)]
        self.build_student_solution(src_list)
        self.wq.changepriority('ex0', 4)
        actual_odd = self.wq.getoddlist()
        actual_even = self.wq.getevenlist()

        src_list = [('ex0', 4), ('ex1', 5)]
        odd, even = split_source(sort_list(src_list))
        expect_odd = build_solution(odd)
        expect_even = build_solution(even)

        self.assertEqual(to_string(expect_odd), to_string(actual_odd),
                         'Failed to change odd head priority, the odd head should become new even head with new priority.')
        self.assertEqual(to_string(expect_even), to_string(actual_even),
                         'Failed to change odd head priority, the odd head should become new even head with new priority.')

    def test_change_even_head_same_priority(self):
        src_list = [('ex0', 10), ('ex1', 5)]
        self.build_student_solution(src_list)
        self.wq.changepriority('ex1', 5)
        actual_odd = self.wq.getoddlist()
        actual_even = self.wq.getevenlist()

        odd, even = split_source(sort_list(src_list))
        expect_odd = build_solution(odd)
        expect_even = build_solution(even)

        self.assertEqual(to_string(expect_odd), to_string(actual_odd),
                         'Failed to change even head priority with same priority.')
        self.assertEqual(to_string(expect_even), to_string(actual_even),
                         'Failed to change even head priority with same priority.')

    def test_change_even_head_higher_priority_remain_even_head(self):
        src_list = [('ex0', 10), ('ex1', 5)]
        self.build_student_solution(src_list)
        self.wq.changepriority('ex1', 8)
        actual_odd = self.wq.getoddlist()
        actual_even = self.wq.getevenlist()

        src_list = [('ex0', 10), ('ex1', 8)]
        odd, even = split_source(sort_list(src_list))
        expect_odd = build_solution(odd)
        expect_even = build_solution(even)

        self.assertEqual(to_string(expect_odd), to_string(actual_odd),
                         'Failed to change even head priority with higher priority than original even head.')
        self.assertEqual(to_string(expect_even), to_string(actual_even),
                         'Failed to change even head priority with higher priority than original even head.')

    def test_change_even_head_higher_priority_to_be_odd_head(self):
        src_list = [('ex0', 10), ('ex1', 5)]
        self.build_student_solution(src_list)
        self.wq.changepriority('ex1', 20)
        actual_odd = self.wq.getoddlist()
        actual_even = self.wq.getevenlist()

        src_list = [('ex0', 10), ('ex1', 20)]
        odd, even = split_source(sort_list(src_list))
        expect_odd = build_solution(odd)
        expect_even = build_solution(even)

        self.assertEqual(to_string(expect_odd), to_string(actual_odd),
                         'Failed to change even head priority, the even head should become new odd head with new priority.')
        self.assertEqual(to_string(expect_even), to_string(actual_even),
                         'Failed to change even head priority, the even head should become new odd head with new priority.')

    def test_change_odd_body_to_odd_head(self):
        src_list = [('ex0', 50), ('ex1', 40), ('ex2', 30), ('ex3', 20), ('ex4', 10)]
        self.build_student_solution(src_list)
        self.wq.changepriority('ex2', 100)
        actual_odd = self.wq.getoddlist()
        actual_even = self.wq.getevenlist()

        src_list = [('ex0', 50), ('ex1', 40), ('ex2', 100), ('ex3', 20), ('ex4', 10)]
        odd, even = split_source(sort_list(src_list))
        expect_odd = build_solution(odd)
        expect_even = build_solution(even)

        self.assertEqual(to_string(expect_odd), to_string(actual_odd),
                         'Failed to change node priority and move from odd body to odd head.')
        self.assertEqual(to_string(expect_even), to_string(actual_even),
                         'Failed to change node priority and move from odd body to odd head.')

    def test_change_odd_body_to_even_head(self):
        src_list = [('ex0', 50), ('ex1', 40), ('ex2', 30), ('ex3', 20), ('ex4', 10)]
        self.build_student_solution(src_list)
        self.wq.changepriority('ex2', 45)
        actual_odd = self.wq.getoddlist()
        actual_even = self.wq.getevenlist()

        src_list = [('ex0', 50), ('ex1', 40), ('ex2', 45), ('ex3', 20), ('ex4', 10)]
        odd, even = split_source(sort_list(src_list))
        expect_odd = build_solution(odd)
        expect_even = build_solution(even)

        self.assertEqual(to_string(expect_odd), to_string(actual_odd),
                         'Failed to change node priority and move from odd body to even head.')
        self.assertEqual(to_string(expect_even), to_string(actual_even),
                         'Failed to change node priority and move from odd body to even head.')

    def test_change_even_body_to_even_head(self):
        src_list = [('ex0', 50), ('ex1', 40), ('ex2', 30), ('ex3', 20), ('ex4', 10)]
        self.build_student_solution(src_list)
        self.wq.changepriority('ex3', 45)
        actual_odd = self.wq.getoddlist()
        actual_even = self.wq.getevenlist()

        src_list = [('ex0', 50), ('ex1', 40), ('ex2', 30), ('ex3', 45), ('ex4', 10)]
        odd, even = split_source(sort_list(src_list))
        expect_odd = build_solution(odd)
        expect_even = build_solution(even)

        self.assertEqual(to_string(expect_odd), to_string(actual_odd),
                         'Failed to change node priority and move from even body to even head.')
        self.assertEqual(to_string(expect_even), to_string(actual_even),
                         'Failed to change node priority and move from even body to even head.')

    def test_change_even_body_to_odd_head(self):
        src_list = [('ex0', 50), ('ex1', 40), ('ex2', 30), ('ex3', 20), ('ex4', 10)]
        self.build_student_solution(src_list)
        self.wq.changepriority('ex3', 100)
        actual_odd = self.wq.getoddlist()
        actual_even = self.wq.getevenlist()

        src_list = [('ex0', 50), ('ex1', 40), ('ex2', 30), ('ex3', 100), ('ex4', 10)]
        odd, even = split_source(sort_list(src_list))
        expect_odd = build_solution(odd)
        expect_even = build_solution(even)
        self.assertEqual(to_string(expect_odd), to_string(actual_odd),
                         'Failed to change node priority and move from even body to odd head.')
        self.assertEqual(to_string(expect_even), to_string(actual_even),
                         'Failed to change node priority and move from even body to odd head.')

    def test_change_odd_body_to_even_body(self):
        src_list = [('ex0', 50), ('ex1', 40), ('ex2', 30), ('ex3', 20), ('ex4', 10)]
        self.build_student_solution(src_list)
        self.wq.changepriority('ex2', 15)
        actual_odd = self.wq.getoddlist()
        actual_even = self.wq.getevenlist()

        src_list = [('ex0', 50), ('ex1', 40), ('ex2', 15), ('ex3', 20), ('ex4', 10)]
        odd, even = split_source(sort_list(src_list))
        expect_odd = build_solution(odd)
        expect_even = build_solution(even)

        self.assertEqual(to_string(expect_odd), to_string(actual_odd),
                         'Failed to change node priority and move from odd body to even body.')
        self.assertEqual(to_string(expect_even), to_string(actual_even),
                         'Failed to change node priority and move from odd body to even body.')

    def test_change_even_body_to_odd_body(self):
        src_list = [('ex0', 50), ('ex1', 40), ('ex2', 30), ('ex3', 20), ('ex4', 10)]
        self.build_student_solution(src_list)
        self.wq.changepriority('ex3', 35)
        actual_odd = self.wq.getoddlist()
        actual_even = self.wq.getevenlist()

        src_list = [('ex0', 50), ('ex1', 40), ('ex2', 30), ('ex3', 35), ('ex4', 10)]
        odd, even = split_source(sort_list(src_list))
        expect_odd = build_solution(odd)
        expect_even = build_solution(even)

        self.assertEqual(to_string(expect_odd), to_string(actual_odd),
                         'Failed to change node priority and move from even body to odd body.')
        self.assertEqual(to_string(expect_even), to_string(actual_even),
                         'Failed to change node priority and move from even body to odd body.')


class TestNegateAll(_TestWackyQueue):

    def test_negate_empty(self):
        self.wq.negateall()
        self.assertIsNone(self.wq.getoddlist(), 'Test failed.')
        self.assertIsNone(self.wq.getevenlist(), 'Test failed.')

    def test_negate_one_odd(self):
        src_list = [('ex0', 10)]
        self.build_student_solution(src_list)
        self.wq.negateall()
        actual_odd = self.wq.getoddlist()
        actual_even = self.wq.getevenlist()

        odd, even = split_source(src_list, negate=True)
        expect_odd = build_solution(odd)
        expect_even = build_solution(even)
        self.assertEqual(to_string(expect_odd), to_string(actual_odd),
                         'Failed to negate the list. Odd node list has incorrect data or incorrect priority.')
        self.assertEqual(to_string(expect_even), to_string(actual_even),
                         'Failed to negate the list. Even node list has incorrect data or incorrect priority.')

    def test_negate_one_odd_one_even(self):
        src_list = [('ex0', -10), ('ex1', 20)]
        self.build_student_solution(src_list)
        self.wq.negateall()
        actual_odd = self.wq.getoddlist()
        actual_even = self.wq.getevenlist()

        odd, even = split_source(src_list, negate=True)
        expect_odd = build_solution(odd)
        expect_even = build_solution(even)
        self.assertEqual(to_string(expect_odd), to_string(actual_odd),
                         'Failed to negate the list. Odd node list has incorrect data or incorrect priority.')
        self.assertEqual(to_string(expect_even), to_string(actual_even),
                         'Failed to negate the list. Even node list has incorrect data or incorrect priority.')

    def test_negate_equal_priority(self):
        src_list = [('A', -10), ('B', -10), ('C', 20)]
        self.build_student_solution(src_list)
        self.wq.negateall()
        actual_odd = self.wq.getoddlist()
        actual_even = self.wq.getevenlist()

        odd, even = split_source(sort_list(src_list, descending=True), negate=True)
        expect_odd = build_solution(odd)
        expect_even = build_solution(even)

        self.assertEqual(to_string(expect_odd), to_string(actual_odd),
                         'Failed to negate the list. Odd node list has incorrect data or incorrect priority.')
        self.assertEqual(to_string(expect_even), to_string(actual_even),
                         'Failed to negate the list. Even node list has incorrect data or incorrect priority.')

    def test_negate_multiple(self):
        src_list = [('ex0', -10), ('ex1', 0), ('ex2', -4), ('ex3', 25), ('ex4', -30), (None, 8), ('ex4', -30)]
        self.build_student_solution(src_list)
        self.wq.negateall()
        actual_odd = self.wq.getoddlist()
        actual_even = self.wq.getevenlist()

        odd, even = split_source(sort_list(src_list), negate=True)
        expect_odd = build_solution(odd)
        expect_even = build_solution(even)
        self.assertEqual(to_string(expect_odd), to_string(actual_odd),
                         'Failed to negate the list. Odd node list has incorrect data or incorrect priority.')
        self.assertEqual(to_string(expect_even), to_string(actual_even),
                         'Failed to negate the list. Even node list has incorrect data or incorrect priority.')


class TestExtractHigh(_TestWackyQueue):

    def test_extract_one_node_positive_priority(self):
        # init
        src_list = [('ex0', 10)]
        self.build_student_solution(src_list)
        actual = self.wq.extracthigh()
        self.assertEqual(src_list[0][0], actual, 'Failed to extract the only node from the WackyQueue.')

    def test_extract_one_node_negative_priority(self):
        # init
        src_list = [('ex0', -10)]
        self.build_student_solution(src_list)
        actual = self.wq.extracthigh()
        self.assertEqual(src_list[0][0], actual, 'Failed to extract the only node from the WackyQueue.')

    def test_extract_two_nodes_positive_priority(self):
        # init
        src_list = [('ex0', 10), ('ex1', 20)]
        self.build_student_solution(src_list)
        actual = self.wq.extracthigh()
        self.assertEqual(src_list[1][0], actual, 'Failed to extract the highest priority node from the WackyQueue.')
        actual = self.wq.extracthigh()
        self.assertEqual(src_list[0][0], actual, 'Failed to extract the highest priority node from the WackyQueue.')

    def test_extract_two_nodes_negative_priority(self):
        # init
        src_list = [('ex0', -20), (None, -10)]
        self.build_student_solution(src_list)
        actual = self.wq.extracthigh()
        self.assertEqual(src_list[1][0], actual, 'Failed to extract the highest priority node from the WackyQueue.')
        actual = self.wq.extracthigh()
        self.assertEqual(src_list[0][0], actual, 'Failed to extract the highest priority node from the WackyQueue.')

    def test_extract_mixed_priority(self):
        # init
        src_list = [(False, float('-inf')), (None, -2), ('csca48a1', 0), (2333, 10), (3.14, 46)]
        self.build_student_solution(src_list)
        actual = self.wq.extracthigh()
        self.assertEqual(src_list[4][0], actual, 'Failed to extract the highest priority node from the WackyQueue.')
        actual = self.wq.extracthigh()
        self.assertEqual(src_list[3][0], actual, 'Failed to extract the highest priority node from the WackyQueue.')
        actual = self.wq.extracthigh()
        self.assertEqual(src_list[2][0], actual, 'Failed to extract the highest priority node from the WackyQueue.')
        actual = self.wq.extracthigh()
        self.assertEqual(src_list[1][0], actual, 'Failed to extract the highest priority node from the WackyQueue.')
        actual = self.wq.extracthigh()
        self.assertEqual(src_list[0][0], actual, 'Failed to extract the highest priority node from the WackyQueue.')


class TestPEP8(unittest.TestCase):
    def test_pep8(self):
        pep8style = pep8.StyleGuide(quiet=True,
                                    ignore=('E121', 'E123', 'E126', 'E133',
                                            'E211', 'E226', 'E241', 'E242', 'E704', 'W503'))
        result = pep8style.check_files(PEP8_CHECK_FILES)

        report_output = "Found code style errors (and warnings):"
        for code in result.messages:
            message = result.messages[code]
            count = result.counters[code]
            report_output += "\n" + code + ": " + message + " (" + str(count) + ")"

        self.assertEqual(result.total_errors, 0, report_output)


# hijack module, detect any restricted calls. Terminated test if detected
# hijack.hijack(a1)

if __name__ == "__main__":
    unittest.main(exit=False, verbosity=2)
