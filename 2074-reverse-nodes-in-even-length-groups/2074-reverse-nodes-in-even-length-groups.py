# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseEvenLengthGroups(self, head: Optional[ListNode]) -> Optional[ListNode]:
        n = 1
        temp = head
        k = 1
        li = []
        while temp:
            m = k
            while m>0 and temp:
                temp = temp.next
                m-=1
            li.append(k-m)
            k+=1
            
        fakeHead = head
        
        prev = head
        i=0
        while head:
            if li[i] % 2 == 0:
                k = li[i]
                curr = None
                reverseHead = ListNode(0)
                save = None
                while k!=0 and head:
                    curr = head
                    head = head.next
                    if k==li[i]:
                        save = curr
                    curr.next = reverseHead.next
                    reverseHead.next = curr
                    k-=1
                prev.next = reverseHead.next
                save.next = head
                prev = save
                # if i+1<len(li) and li[i] % 2==0 and li[i+1]%2==0:
                #     prev = head
            else:
                k = li[i]
                for _ in range(k):
                    if not head: break
                    prev = head
                    head = head.next
                    
            i += 1
        return fakeHead