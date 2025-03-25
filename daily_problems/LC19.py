#https://leetcode.cn/problems/remove-nth-node-from-end-of-list/description/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head.next:
            return None

        slow, fast = head, head
        for _ in range(n):
            fast = fast.next

        if not fast:
            return slow.next

        prev = slow
        slow, fast = slow.next, fast.next
        while fast:
            prev, slow, fast = prev.next, slow.next, fast.next

        prev.next = slow.next
        return head