# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = sub = ListNode(0, head)
        
        for _ in range(1, left):
            sub = sub.next
        
        first = sub.next
        for _ in range(right-left):
            second = first.next
            first.next, second.next, sub.next = second.next, sub.next, second
        
        return dummy.next