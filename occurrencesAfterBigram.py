#leetcode Problem

class Solution:
    def findOcurrences(self, text: str, first: str, second: str) -> List[str]:
        temp=text.split(" ")
        ans=[]
        
        for i in range(2,len(temp)):
            if temp[i-2]==first and temp[i-1]==second:
                ans.append(temp[i])
        return ans
