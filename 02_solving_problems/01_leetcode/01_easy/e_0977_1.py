class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        return sorted([abs(i * i) for i in nums])