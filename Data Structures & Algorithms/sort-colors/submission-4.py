class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        #같은 숫자끼리 그룹화해서 오름차순으로 정렬하라.
        #입력:list[int]
        #출력:없음 제자리 변환

        left=0
        current=0
        right=len(nums)-1
        
       

        while(current<=right):
            
            if nums[current]==0:
                nums[left],nums[current]=nums[current],nums[left]
                left+=1
                current+=1

            elif nums[current]==1:
                current+=1

            elif nums[current]==2:
                nums[current],nums[right]=nums[right],nums[current]
                right-=1

                

           

           