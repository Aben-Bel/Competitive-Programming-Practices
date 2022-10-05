class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        prefix = [0]
        for i in range(len(cardPoints)):
            prefix.append(prefix[-1]+cardPoints[i])
        
        
        m = 1
        left = 0
        right = len(prefix)-k-1
        while right < len(prefix):
            m = max(m, prefix[left] + (prefix[-1] - prefix[right]))
            left += 1
            right += 1
        
        return m