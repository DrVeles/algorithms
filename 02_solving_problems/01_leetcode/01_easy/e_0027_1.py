class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        left, right = 0, len(nums)

        while left < right:
            if nums[left] == val:
                right -= 1
                nums[left], nums[right] = nums[right], nums[left]
            else:
                left += 1
        
        return right

# OK 16%, 91%