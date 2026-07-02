class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        for i in range(0,len(nums)):
            last_num=nums.pop()
            if last_num in nums:
                return True
        
        return False