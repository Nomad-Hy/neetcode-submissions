class Solution:
    
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
        
        

