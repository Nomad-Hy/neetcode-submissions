class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        idx_dict={}
        result=[]

        for idx,num in enumerate(nums):
            

            if target-num in idx_dict:
                
                result.append(idx_dict[target-num])
                result.append(idx)

                return result
                   
            idx_dict[num]=idx
        
                


            

            
     