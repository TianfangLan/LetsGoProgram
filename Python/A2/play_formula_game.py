"""
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
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this file.  If not, see <http://www.gnu.org/licenses/>.
"""

from formula_tree import FormulaTree, Leaf, NotTree, AndTree, OrTree
from formula_game_functions import build_tree, evaluate, play2win

def get_formula():
    got_good_formula = False
    while not got_good_formula:
        formula = input("Please enter formula: ")
        root = build_tree(formula)
        got_good_formula = (root != None)
        if not got_good_formula:
            print("invalid formula")
    return (formula, root)

def get_variables(formula):
    got_good_variables = False
    while not got_good_variables:
        variables = input("Please enter order of variables to assign: ")
        got_good_variables = True
        for x in variables:
            if not (x in formula):
                print("variable", x, "not in formula")
                got_good_variables = False
            elif (variables.count(x) > 1):
                print("variable", x, "appears more than once")
                got_good_variables = False
        for c in formula:
            if c.islower() and not (c in variables):
                print("variable", c, "not entered")
                got_good_variables = False
    return variables

def get_turns(num_variables):
    got_good_turns = False
    while not got_good_turns:
        turns = input("Please enter turns of players E and A: ")
        got_good_turns = True
        for p in turns:
            if p != 'E' and p != 'A':
                print(p, "is not a valid player")
                got_good_turns = False
        if len(turns) > num_variables:
            print("too many turns for number of variables")
            got_good_turns = False
        elif len(turns) < num_variables:
            print("too few turns for number of variables")
            got_good_turns = False
    return turns

def get_value(turns, variables, currturn):
    got_good_newval = False
    while not got_good_newval:
        newval = input("Player " + turns[currturn] +
                       " please enter value for variable " +
                       variables[currturn] + "[0/1/C(omputer)]: ")
        got_good_newval = (len(newval)==1) and (newval in "01C")
        if not got_good_newval:
            print("enter just one symbol (0 or 1 or C)")
    return newval

def play_game():
    (formula, root) = get_formula()

    variables = get_variables(formula)

    turns = get_turns(len(variables))

    values = ""
    for i in range(len(turns)):
        print("Turn", i)
        print("Formula:", formula)
        print("Turns:        ", turns)
        print("Variables:    ", variables)
        print("Values played:", values)
        newval = get_value(turns, variables, i)
        if newval == 'C':
            newval = str(play2win(root, turns, variables, values))
        values = values + newval

    print("Game over")
    print("Formula:", formula)
    print("Turns:        ", turns)
    print("Variables:    ", variables)
    print("Values played:", values)
    if evaluate(root, variables, values) == 1:
        winner = 'E'
    else:
        winner = 'A'
    print("Player", winner, "wins!")

if __name__ == "__main__":
    play_game()
