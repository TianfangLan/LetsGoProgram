"""
# Tianfang Lan
# Copyright Nick Cheng, 2016, 2018
# Distributed under the terms of the GNU General Public License.
#
# This file is part of Assignment 2, CSCA48, Winter 2018
#
# This is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This file is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this file. If not, see <http://www.gnu.org/licenses/>.
"""

# Do not change this import statement, or add any of your own!
from formula_tree import FormulaTree, Leaf, NotTree, AndTree, OrTree

# Do not change any of the class declarations above this comment.

# Add your functions here.


def build_tree(formula):
    ''' (str) -> FormulaTree or None
    The funcion will take in a string formula and return the formula in the
    form of FormulaTree. If the formula is not a valid one, the function will
    return None.
    REQ: formula should only be a string
    REQ: formula should only contain "-", "+", "*", lower case letter
    REQ: '(' or ')'
    >>> build_tree('(a*b)')
    AndTree(Leaf('a'), Leaf('b'))
    >>> build_tree('((a*b)+d)')
    OrTree(AndTree(Leaf('a'), Leaf('b')), Leaf('d'))
    >>> build_tree('(x+y*z)')
    None
    '''
    # current is the position of the certain connective in the formula
    current = None
    # connect is the either the connective is '+' or '*'
    connect = None
    # represent current position
    posi = 0
    # number of left and right parentheses
    number_l = 0
    number_r = 0
    # number of connectives
    number_c = 0
    # find the number of lower character in the string
    number_letter = 0
    # loop the letters in the formula if it is not empty
    # find the position when the enter string is not empty
    if (len(formula) != 0):
        # find the certain connective and its position of the input formula
        for char in formula:
            # another important limit is number of connectives should equals to
            # pairs of parentheses
            if (char == '('):
                number_l += 1
            elif (char == ')'):
                number_r += 1
            elif (char == '*' or char == '+'):
                number_c += 1
            elif (char.islower()):
                number_letter += 1
            # only when it reaches char is a connective and parentheses
            # are paird
            if ((char == '+' or char == '*') and
                formula[:posi].count('(') - 1 == formula[:posi].count(')') and
                    formula[posi:].count('(') + 1 ==
                    formula[posi:].count(')')):
                # store the connective
                connect = char
                # store the position of the connective
                current = posi
            posi += 1
    # limit the invalid formula with current and connect
    # 1.if the parentheses is not paired
    # 2.one parenthese can only contain one connective
    # so pair should equal to connectives
    # 3. variables should be connected to each other with a connective
    # so connective should be 1 less then the number of lower letters
    if (number_l != number_r or number_l != number_c or
            number_letter - 1 != number_c):
        connect = None
        current = None
    # ____start to do with the recursion
    # first do the special case when input is an empty string
    if (len(formula) == 0):
        result = None
    # when the formula only contains one varible (smallest case)
    # Note: because only lower case letter can be a leaf.
    elif (formula[0].islower() and len(formula) == 1):
        # the lower case letter should only be the leaf of the formulatree.
        result = Leaf(formula)
    # when it comes to a NotTree
    elif (len(formula) > 1 and formula[0] == '-' and formula[1] != ')'):
        result = NotTree(build_tree(formula[1:]))
        # Note: once there is an invalid child, CUT the current tree
        if (None in result.get_children()):
            result = None
    # limit the result with connect and current
    elif (connect is None or current is None):
        result = None
    # when current formula is connected with AND
    elif (formula[0] == '(' and connect == '*'):
        # do the formula in 2 parts
        result = AndTree(build_tree(formula[1:current]),
                         build_tree(formula[current + 1:-1]))
        # Note: once there is an invalid child, CUT the current tree
        if (None in result.get_children()):
            result = None
    # when current formula is connected with OR
    elif (formula[0] == '(' and connect == '+'):
        result = OrTree(build_tree(formula[1:current]),
                        build_tree(formula[current + 1:-1]))
        # Note: once there is an invalid child, CUT the current tree
        if (None in result.get_children()):
            result = None
    else:
        result = None
    return result


def simplify_tree(root):
    '''(FormulaTree) -> FormulaTree
    this function is a helper function to modify the input Tree. It will change
    the cases when AND node is a child of an And node or Or node is a child of
    an Or node.
    REQ: the input should be a FormulaTree
    >>> simplify_tree(AndTree(Leaf('a'), AndTree(Leaf('b'), Leaf('c'))))
    FormulaTree ('+', ['a', 'b', 'c'])
    '''
    # set the current symbol and it's children
    cur_sym = None
    cur_chi = None
    # if input is not a FormulaTree
    if (not isinstance(root, FormulaTree)):
        result = None
    # when it is not, get the symbol and it's children
    else:
        # Note: cur_sym should always be a string of the symbol
        cur_sym = root.get_symbol()
        # Note: cur_shi should always be a list
        cur_chi = root.get_children()
        # Note: num_chi should always be a int
        num_chi = len(cur_chi)
    # judge the symbol of the root
    if (cur_sym == '+' or cur_sym == '*'):
        # set a final list for setting the new root
        new_list = []
        # check all the children in the list of current root
        for child in cur_chi:
            # check if the child's symbol equals to the current symbol
            # if it is the leaf, append it to the new_list
            if (isinstance(child, Leaf)):
                new_list.append(child)
            # if the child is not leaf and does not equals to the cur_sym
            elif (child.get_symbol() != cur_sym):
                # child should still be simpled
                result = simplify_tree(child)
                # append the result to the new_list
                new_list.append(result)
            # Note: cur_sym can only be '+' or '*'
            elif (child.get_symbol() == cur_sym):
                # The children list will be bigger in this case
                new_list += simplify_tree(child).get_children()
        result = FormulaTree(cur_sym, new_list)
    elif (isinstance(root, Leaf)):
        result = root
    elif (isinstance(root, NotTree)):
        result = FormulaTree('-', root.get_children())
    else:
        result = None
    return result


def draw_formula_tree(root):
    '''(FormulaTree) -> str
    The function will take in a FormulaTree and return a string which draws the
    formula Tree.
    REQ: the input root should be a formulatree
    >>> draw_formula_tree(OrTree(AndTree(Leaf('a'), Leaf('b')), Leaf('d')))
    + d
      * b
        a
    '''
    result = draw_tree_helper(root, 1)
    return result


def draw_tree_helper(root, deep):
    '''(FormulaTree, int) -> str
    For this helper, deep means how deep the current formula is. It is for
    judging how many space should make before the line, deep default to be 1.
    '''
    # do the smallest case first
    if (isinstance(root, Leaf)):
        # it is a Leaf get the symbol of it
        result = root.get_symbol()
    # do the case when it is a NotTree
    elif (isinstance(root, NotTree)):
        result = root.get_symbol()
        result += ' ' + draw_tree_helper(root.get_children()[0], deep + 1)
    # when the input root is other cases of FormulaTree
    elif (isinstance(root, FormulaTree)):
        child_list = root.get_children()
        # loop all the children in the list
        # the first line is special for the formula, add before the loop
        result = root.get_symbol() + ' ' + \
            draw_tree_helper(child_list[-1], deep + 1)
        for child in child_list[::-1][1: len(child_list)]:
            # deep counts how deep the formula is, if it is the biggest formula
            # there should be only 2 blanks before the character
            blank = ' ' * 2 * deep
            # do the recursion, since the formula go deeper, deep should plus 1
            result += '\n' + blank + draw_tree_helper(child, deep + 1)
    else:
        result = None
    return result


def evaluate(root, variables, values):
    '''(FormulaTree, str, str) -> int(0 or 1)
    The function will take in a a FormulaTree rooted at root, and a string
    represent the variables, and an int represent the corresponding variables.
    The function will return a int represent the true variable of the whole
    formula.
    REQ: root should be a FormulaTree
    REQ: variables should only be in the root
    REQ: values should have the same length with variables
    REQ: values should be make up with 1s and 0s
    >>>evaluate(OrTree(AndTree(Leaf('a'), Leaf('b')), Leaf('d')), 'abd', '101')
    1
    '''
    # do the smallest case
    if (isinstance(root, Leaf)):
        # get the variable of current leaf
        vari = root.get_symbol()
        # get the position of current vari the variables
        position = variables.find(vari)
        # find the corresponding value for the vari and turn it into an int
        value = values[position]
        result = int(value)
    # we have to deal with the case when several variables are connected with
    # all And, Or or Not, so use the FormulaTree.
    elif (isinstance(root, FormulaTree)):
        # get the symbol(connective) of the FormulaTree.
        con = root.get_symbol()
        # get the children of the root
        child_list = root.get_children()
        # create a new list for all children are fully evaluated
        new_list = []
        # loop all children in the list
        for child in child_list:
            new_list.append(evaluate(child, variables, values))
        # if the connective is Or
        if (con == '+'):
            # find the max in the list
            result = max(new_list)
        elif (con == '*'):
            # find the min value in the list
            result = min(new_list)
        elif (con == '-'):
            result = 1 - evaluate(root.get_children()[0], variables, values)
    else:
        result = None
    return result


def play2win(root, turns, variables, values):
    '''(FormulaTree, str, str, str) -> int(1 or 0)
    The function will return the 'winning' move for the current player, if
    there is not a really winning step (no difference between enter 1 or 0),
    then for player A return 0, for player E return 1.
    REQ: length of turns and variables should ALWAYS be the same.
    REQ: length of turns should ALWAYS be longer than length of values
    >>> play2win(build_tree('((x+y)*((y+z)*(-y+-z)))'), 'EEA', 'xyz', '01')
    0
    '''
    if (len(values) < len(variables)):
        # find which play is using the function
        cheater = turns[len(values)]
    else:
        cheater = None
    # get the goal of cheater
    if (cheater == 'E'):
        result = 1
        goal = 1
    elif (cheater == 'A'):
        result = 0
        goal = 0
    else:
        result = None
        goal = None
    # get the ways to win if cheater enter 1
    to_win1 = playhelper(root, goal, variables, values+'1')
    to_win0 = playhelper(root, goal, variables, values+'0')
    if (to_win1 > to_win0):
        result = 1
    elif (to_win1 < to_win0):
        result = 0
    return result


def playhelper(root, goal, variables, values):
    '''(FormulaTree, int, str, str, int) -> int(cases to win the game)
    the helper function will return the possible ways to get the goal in
    the certain condition
    REQ: goal should only be 0 or 1
    >>> playhelper(build_tree('((x+y)*((y+z)*(-y+-z)))'), 0, 'xyz', '01')
    2
    '''
    # set the default result to be 0
    result = 0
    # when it comes to the smallest case
    if (len(variables) != 0 and len(variables) == len(values)):
        # get the answer of the current formula with full value
        ans = evaluate(root, variables, values)
        # in this case ans should either be 1 or 0, make judge by input goal
        # only when it equals the goal, the case should plus 1 (means we
        # have one more case to reach the goal
        if (ans == goal):
            result = 1
    # this is when the when the game hasn't ended
    elif (len(variables) > len(values)):
        result += playhelper(root, goal, variables, values+'0')
        result += playhelper(root, goal, variables, values+'1')
    return result
