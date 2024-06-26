class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-el for el in stones]
        heapq.heapify(stones)
        
        while len(stones) > 1:
            heapq.heappush(stones, heapq.heappop(stones) - heapq.heappop(stones))
        
        return -stones[0]

#OK 49%, 89%