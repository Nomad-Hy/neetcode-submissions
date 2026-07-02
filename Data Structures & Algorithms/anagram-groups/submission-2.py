

class Solution:

    '''
    첫번째 풀이

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict_list=[]
        result=[]

        for word in strs:
            dictionary={}

            
            

            for char in word:
                
                dictionary[char]=1+dictionary.get(char,0)
            
            if dictionary in dict_list:
                index=dict_list.index(dictionary)
                result[index].append(word)

            else:
                result.append([word])

                dict_list.append(dictionary)

            
                
        return result
    '''    
    
    #더 효율적으로 만든 풀이
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        result=defaultdict(list)

        for word in strs:
            count=[0]*26

            for char in word:
                count[ord(char)-ord('a')]+=1
            
            result[tuple(count)].append(word)

        print(result.values())
        
        return list(result.values())



