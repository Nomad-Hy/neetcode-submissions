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

    def isAnagram(self, s: str, t: str) -> bool: #정렬을 이용한 방식
        if sorted(s)==sorted(t):
            return True
        else:
            return False
       