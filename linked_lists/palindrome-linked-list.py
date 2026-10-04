# LeetCode #234 (Easy): https://leetcode.com/problems/palindrome-linked-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode | None) -> bool:
        stack = []
        curr = head
        curr2 = head

        while curr:
            stack.append(curr.val)
            curr = curr.next

        while curr2:
            val = curr2.val
            if val != stack.pop():
                return False
            curr2 = curr2.next
        return True
