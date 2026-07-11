class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        

        standard=strs[0]

        for i in range(len(standard)):

            char=standard[i]
            for word in strs[1:]:
                if i>=len(word) or word[i]!=char:
                    return word[:i]
        
        return standard