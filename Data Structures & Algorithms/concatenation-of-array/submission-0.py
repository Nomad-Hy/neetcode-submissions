class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        print(nums)

        n=len(nums)
        print(n)
        
        ans=[0]*2*n
        
        for i in range(0,n):
            ans[i]=nums[i]
           
            ans[i+n]=nums[i]
            

        return ans