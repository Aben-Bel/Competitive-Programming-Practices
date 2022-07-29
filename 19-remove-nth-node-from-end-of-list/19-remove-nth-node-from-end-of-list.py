# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head.next:
            return None
    
        ans = ListNode(0,head)
        save = ans
        ahead = head
        while n>0 and ahead:
            ahead = ahead.next
            n-=1
        
        while ahead:
            ans = ans.next
            ahead = ahead.next
        
        ans.next = ans.next.next
        return save.next