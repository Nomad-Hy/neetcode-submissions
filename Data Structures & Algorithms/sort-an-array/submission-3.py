class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        
        return self.merge_sort(nums)
    
    def merge_sort(self,values:List[int])->List[int]:

        if len(values)<=1:
            return values

        middle=len(values)//2

        left=self.merge_sort(values[:middle])
        right=self.merge_sort(values[middle:])

        return self.merge_sorted(left,right) 

    def merge_sorted(self,left:List[int],right:List[int])->List[int]:
        
        sorted_list=[]
        left_point=0
        right_point=0

        while(left_point<len(left) and right_point<len(right)):
            if left[left_point]<=right[right_point]:
                sorted_list.append(left[left_point])
                left_point+=1
            else:
                sorted_list.append(right[right_point])
                right_point+=1
            
        
        sorted_list.extend(left[left_point:])
        sorted_list.extend(right[right_point:])

        return sorted_list

