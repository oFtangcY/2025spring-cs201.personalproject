#pre-problem

#Solution 1
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        vals = []
        curr_node = head

        while curr_node is not None:
            vals.append(curr_node.val)
            curr_node = curr_node.next

        return vals == vals[::-1]

#Solution 2

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next:
            return True

        fast = head.next
        slow = head
        while fast != None and fast.next != None:
            fast = fast.next.next
            slow = slow.next

        prev = slow
        while slow:
            next = slow.next
            slow.next = prev
            prev = slow
            slow = next

        left, right = head, prev
        while left.next != right and left != right:
            if left.val == right.val:
                left, right = left.next, right.next
            else:
                return False

        return True

