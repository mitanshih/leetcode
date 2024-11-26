
'''2058. Find the Minimum and Maximum Number of Nodes Between Critical Points
Created on 2024-07-05 17:13:18

@author: MilkTea_shih
'''

#%%    Packages
from typing import Callable, Optional

#%%    Variable
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

#%%    Functions
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]
                                   ) -> list[int]:
        '''Find `critical_value` and calculate `minimum_distance`, 
        then return the correct answer, which means `minimum_distance`
        not equals infinity.
        '''
        assert head is not None  # There is at least 2 nodes in `head`.
        previous_value: int = head.val
        head = head.next
        assert isinstance(head, ListNode)

        critical_point: list[int] = []
        minimum_distance: float = float('inf')
        index: int = 1
        while isinstance(head.next, ListNode):
            next_value: int = head.next.val
            if ((previous_value < head.val and head.val > next_value)
                    or (previous_value > head.val and head.val < next_value)):
                if critical_point:
                    minimum_distance = min(minimum_distance,
                                           index - critical_point[-1])

                critical_point.append(index)

            previous_value = head.val
            head = head.next
            index += 1

        if minimum_distance == float('inf'):
            #length of `critical_value` is smaller than 2,
            # so distance isn't exist.
            return [-1, -1]  #default value
        return [int(minimum_distance), critical_point[-1] - critical_point[0]]

class Solution_:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]
                                   ) -> list[int]:
        '''Find `critical_value` first, then calculate the distance.
        '''
        assert head is not None  # There is at least 2 nodes in `head`.
        previous_value: int = head.val
        head = head.next

        critical_point: list[int] = []
        index: int = 1
        while head is not None and isinstance(head.next, ListNode):
            next_value: int = head.next.val
            if ((previous_value < head.val and head.val > next_value)
                    or (previous_value > head.val and head.val < next_value)):
                critical_point.append(index)

            previous_value = head.val
            head = head.next
            index += 1

        if len(critical_point) > 1:
            maximum_distance: int = critical_point[-1] - critical_point[0]

            minimum_distance: int = maximum_distance
            for index in range(len(critical_point) - 1):
                temp: int = critical_point[index + 1] - critical_point[index]
                if temp < minimum_distance:
                    minimum_distance = temp
            return [minimum_distance, maximum_distance]

        return [-1, -1]

#%%    Main Function


#%%    Main
if __name__ == '__main__':
    pass

#%%
