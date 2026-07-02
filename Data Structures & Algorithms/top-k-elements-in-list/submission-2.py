class Solution:
    '''
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_dict={}

        for num in nums:
            num_dict[num]=1+num_dict.get(num,0)
        
        arr=[]
        for num,cnt in num_dict.items():
            arr.append([cnt,num])

        arr.sort()

        res=[]

        for i in range(k):
            res.append(arr.pop()[1])
        
        
        return res
    '''

    '''
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        num_dict={}

        for num in nums:
            num_dict[num]=1+num_dict.get(num,0)

        arr=[]

        for num,cnt in num_dict.items():
            heapq.heappush(arr,(cnt,num))

            if len(arr)>k:
                heapq.heappop(arr)

        res=[]

        for i in range(k):
            res.append(heapq.heappop(arr)[1])

        return res
    '''

    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count={}
        freq=[[]for i in range(len(nums)+1)]

        for n in nums:
            count[n]=1+count.get(n,0)

        for n,c in count.items():
            freq[c].append(n)

        res=[]

        for i in range(len(freq)-1,0,-1):
            for n in freq[i]:
                res.append(n)
                if len(res)==k:
                    return res