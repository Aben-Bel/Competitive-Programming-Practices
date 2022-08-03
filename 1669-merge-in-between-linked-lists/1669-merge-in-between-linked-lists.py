# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        storeA = list1
        storeB = list2
        
        while a>1:
            list1 = list1.next
            a -= 1
            b -= 1
        l1 = list1
        
        while b>0:
            list1 = list1.next
            b -= 1
            
        while list2 and list2.next:
            list2 = list2.next
        
        list2.next = list1.next
        l1.next = storeB
        return storeA
        