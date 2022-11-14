class Solution:
    def maxProfit(self, inventory: List[int], orders: int) -> int:
        inventory.sort(reverse=True)
        inventory.append(0)
        # [5,5,5,5,5,4,4,4,1,1,1]
        #  l                    r
        left = 0
        cur = inventory[0]
        profit = 0
        for right in range(1,len(inventory)):
            if cur != inventory[right]:
                width = (right - left)
                if width*(cur-inventory[right]) < orders:
                    dif = inventory[right]
                    n1 = cur*(cur+1)//2
                    n2 = dif*(dif+1)//2
                    profit += width*(n1-n2)
                    orders -= width*(cur - dif)
                    cur = dif
                else:
                    depth = orders//width
                    dif = cur - depth
                    n1 = cur*(cur + 1)//2
                    n2 = dif*(dif + 1)//2
                    profit += width*(n1-n2)
                    cur -= depth
                    orders -= width*depth
                    profit += (orders)*cur
                    break
                    
            
        return profit % 1000000007