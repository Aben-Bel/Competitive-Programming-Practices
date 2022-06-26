class Solution:
    def countHousePlacements(self, n: int) -> int:
        first, second = 1,1
        k = n
        while n>0:
            first, second = second, first+second
            n-=1
            
        return (second**2)%1000000007
        # (1| ) ( |1) ( | ) (1|1)
        # 1->2 2^2
        # 2->9 3^2
        # 3->25 5^2
        # 4->49 8^2
        # 5->169 13^2
        
        # (1| ) ( |1) ( | ) (1| ) ( | )
        # ( |1) (1| ) ( | ) ( | ) (1| )
        
        # space = n*2 , alternate = 
        # (1|1) ( |1) (1| ) (1| ) ( | ) (1| ) ( | ) ( | ) (1| )
        # ( | ) (1| ) ( | ) ( | ) (1| ) (1| ) ( | ) ( | ) (1| )
        # (1| ) ( |1) ( | ) ( | ) (1| ) (1| ) ( | ) ( | ) (1| )
        
        
        
        
        
        