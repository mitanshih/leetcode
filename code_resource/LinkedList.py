'''reference
https://www.geeksforgeeks.org/reverse-a-linked-list/
https://walkccc.me/LeetCode/problems/234/#__tabbed_1_3

https://leetcode.com/problems/palindrome-linked-list/?envType=daily-question&envId=2024-03-22

https://web.ntnu.edu.tw/~algo/Palindrome.html
'''


class Node:
    # Constructor to initialize the node object
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    # Function to initialize head
    def __init__(self):
        self.head = None

    # Function to reverse the linked list
    def reverse(self):
        prev = None
        current = self.head
        while (current is not None):
            next = current.next
            current.next = prev
            prev = current
            current = next
        self.head = prev

    # Function to insert a new node at the beginning
    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    # Utility function to print the LinkedList
    def printList(self):
        temp = self.head
        while temp is not None:
            print(temp.data, end=" ")
            temp = temp.next


# Driver code
linked_list = LinkedList()
linked_list.push(20)
linked_list.push(4)
linked_list.push(15)
linked_list.push(85)

print ("Given linked list")
linked_list.printList()
linked_list.reverse()
print ("\nReversed linked list")
linked_list.printList()
