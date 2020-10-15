class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        ind=0
        n=len(bits)
        
        while ind<n:
            if ind==n-1 and bits[ind]==0:
                return True
            if bits[ind]==1:
                ind+=2
            else:
                ind+=1
        return False
