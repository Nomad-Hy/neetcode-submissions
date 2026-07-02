class Solution:
    
    '''def isAnagram(self, s: str, t: str) -> bool:
        # 해쉬를 이용한 방법 --> 해시충돌 가능성도 생각해야함
        total=0

        for char in s:
            total+=hash(char)

        for char in t:
            total-=hash(char)

        if total==0:
            return True
        else:
            return False
    '''

    '''
    def isAnagram(self, s: str, t: str) -> bool: #정렬을 이용한 방식
        if sorted(s)==sorted(t):
            return True
        else:
            return False
    '''

    def isAnagram(self, s: str, t: str) -> bool: #해시 충돌 방지 
        if len(s)!=len(t):
            return False

        countS,countT={},{}

        for i in range(len(s)):
            countS[s[i]]=1+countS.get(s[i],0) #빈도수 저장
            countT[t[i]]=1+countT.get(t[i],0)

        return countS==countT


    
       