class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        n=len(nums)
        
        combination=dict()
        for i in range(n):
            if (target-nums[i]) in combination:
                return [combination[target-nums[i]],i]
            combination[nums[i]]=i
        print(combination)

        