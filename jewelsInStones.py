class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        temp={}
        count=0
        
        for i in S:
            if i in temp:
                temp[i]+=1
            else:
                temp[i]=1
        
        for k in J:
            if k in temp:
                count+=temp[k]
        return count
