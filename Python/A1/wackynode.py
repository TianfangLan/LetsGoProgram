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
"""


# You will not be submitting this file.
# So make changes only for your own testing purposes.

class WackyNode:
    """A node for linked lists in a WackyQueue."""

    def __init__(self: 'WackyNode',
                 item: object, priority: int) -> None:
        self._next = None
        self._item = item
        self._priority = priority

    def __str__(self):
        data = ''
        curr = self
        while curr:
            data += '({1}, {0})-->'.format(curr.get_item(), curr.get_priority())
            curr = curr.get_next()
        return data.strip('-->')

    def get_next(self: 'WackyNode') -> 'WackyNode':
        return self._next

    def set_next(self: 'WackyNode', next: 'WackyNode') -> None:
        self._next = next

    def get_item(self: 'WackyNode') -> object:
        return self._item

    def set_item(self: 'WackyNode', item: object) -> None:
        self._item = item

    def get_priority(self: 'WackyNode') -> int:
        return self._priority

    def set_priority(self: 'WackyNode', priority: int) -> None:
        self._priority = priority
