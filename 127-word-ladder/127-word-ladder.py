class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        possibilities = defaultdict(set)
        
        for word in wordList:
            for i in range(len(word)):
                nextWord = word[:i] + "*" + word[i+1:]
                possibilities[nextWord].add(word)
                
        queue = deque()
        queue.append(beginWord)
        level = 0
        visited = set()
        while queue:
            size = len(queue)
            while size > 0:
                currWord = queue.popleft()
                if currWord == endWord:
                    return level+1
                
                for i in range(len(currWord)):
                    nextWord = currWord[:i] + "*" + currWord[i+1:]
                    for word in possibilities[nextWord]:
                        if word in visited:
                            continue
                        queue.append(word)
                        visited.add(word)
                
                size -= 1
            level += 1
            
        return 0
                