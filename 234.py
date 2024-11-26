
'''234. Palindrome Linked List
Created on 2024-03-22 18:41:52
Learned end 2024-03-22 20:39:13
Created on 2024-04-14 16:27:45
2024-04-14 17:18:21


@author: MilkTea_shih
'''

#%%    Packages
from typing import Optional

#%%    Variable

# Definition for singly-linked list.
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
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        head_stop_at_mid: Optional[ListNode] = head
        two_step: Optional[ListNode] = head
        while two_step is not None and two_step.next is not None:
            head_stop_at_mid = head_stop_at_mid.next  # type: ignore

            two_step = two_step.next.next

        reversed_head: Optional[ListNode] = None
        while head_stop_at_mid is not None:
            temp = head_stop_at_mid.next
            head_stop_at_mid.next = reversed_head
            reversed_head = head_stop_at_mid
            head_stop_at_mid = temp

        while head is not None and reversed_head is not None:
            if head.val != reversed_head.val:
                return False
            head = head.next
            reversed_head = reversed_head.next

        return True


#%%    Main Function
print(Solution().isPalindrome(ListNode([1, 2])))

#%%    Main
if __name__ == '__main__':
    pass

#%%
class Solution_:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        temp: list[list[int]] = []
        while head:
            temp.append(head.val)
            #print(head.val)
            head = head.next

        value_list: list[int] = temp[0]
        for i in range(len(value_list) // 2 + len(value_list) % 2):
            if value_list[i] != value_list[-i - 1]:
                return False

        return True


print(Solution_().isPalindrome(ListNode([1, 2])))
