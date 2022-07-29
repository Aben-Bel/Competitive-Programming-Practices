# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getLength(self,head):
        length = 0
        while head:
            head = head.next
            length += 1
        return length
    
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head: return head
        length = self.getLength(head)
        k = k%length
        
        first = head
        second = head
        while k>0:
            second = second.next
            k-=1
        
        while second and second.next:
            first = first.next
            second = second.next
        
        second.next = head
        ans = first.next
        first.next = None
        
        return ans