class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counts=dict()

        for num in nums:
            if num not in counts:
                counts[num]=1
            else:
                counts[num]+=1

        for num,count in counts.items():
            print(f'{num},{count}')
            if count>=len(nums)/2:
                return int(num)