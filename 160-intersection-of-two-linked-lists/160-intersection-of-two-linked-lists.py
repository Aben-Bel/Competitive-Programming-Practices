# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        ptrA = headA
        ptrB = headB
        
        while ptrA and ptrB:
            ptrA = ptrA.next
            ptrB = ptrB.next
        
        if ptrA:
            ptrB = headA
            while ptrA and ptrB:
                ptrA = ptrA.next
                ptrB = ptrB.next
            ptrA = headB
        else:
            ptrA = headB
            while ptrB and ptrA:
                ptrB = ptrB.next
                ptrA = ptrA.next
            ptrB = headA
        
        while ptrA and ptrB and (ptrA != ptrB):
            ptrA = ptrA.next
            ptrB = ptrB.next
        
        if ptrB == ptrA:
            return ptrB
        return None
            
            