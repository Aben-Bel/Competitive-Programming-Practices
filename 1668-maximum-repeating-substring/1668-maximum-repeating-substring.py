class Solution:
    def maxRepeating(self, sequence: str, word: str) -> int:
        maximum = 0
        for k in range(len(sequence)):
            j = 0
            count = 0
            for i in range(k, len(sequence)):
                if word[j] != sequence[i]:
                    maximum = max(maximum, count)
                    count = 0
                    break
                elif word[j] == sequence[i] and j == len(word)-1:
                    count += 1

                j += 1
                j %= len(word)
        
            maximum = max(maximum, count)
        return maximum
                