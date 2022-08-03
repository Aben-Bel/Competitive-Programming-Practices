# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        first = head
        second = head
        
        ck = k
        while ck>1:
            first = first.next
            ck-=1
            
        behind = head
        cur = first.next
        while cur:
            cur = cur.next
            behind = behind.next
            
        first.val, behind.val = behind.val, first.val
        return head
        
        