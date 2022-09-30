# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or head.next == None:
            return head
        
        reverseHead = self.reverseList(head.next)
        tail = head.next
        tail.next = head
        head.next = None
        return reverseHead