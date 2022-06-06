# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        li = []
        cur = head
        while cur:
            li.append(cur)
            cur = cur.next
        left-=1
        right-=1
        while left<right:
            li[left],li[right] = li[right],li[left]
            left+=1
            right-=1
        
        for i in range(len(li)):
            if i+1<len(li):
                print(i)
                li[i].next = li[i+1]
        li[-1].next = None
        
        return li[0]
        