from collections import deque


class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        
        return self._merge_sort(nums)
    
    def _merge_sort(self,values:List[int])->List[int]:
        #입력: 리스트 
        #출력: 정렬된 리스트

        if len(values)<=1:
            return values

        middle=len(values)//2

        left=self._merge_sort(values[:middle])
        right=self._merge_sort(values[middle:])

        return self._merge_sorted(left,right)

    def _merge_sorted(self,left:List[int],right:List[int])->List[int]:

        result=[]

        left_point=0
        right_point=0

        while(left_point<len(left)and right_point<len(right)):

            if left[left_point]<=right[right_point]:
                result.append(left[left_point])
                left_point+=1
            else:
                result.append(right[right_point])
                right_point+=1

        
        result.extend(left[left_point:])
        result.extend(right[right_point:])

        return result
                



        
