class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        ans=[]
        
        for i in range(left,right+1):
            if self.isDivide(i):
                ans.append(i)
        return ans
    def isDivide(self,num):
        s=str(num)
        
        for nums in s:
            if nums=='0' or num%int(nums)!=0:
                return False
        return True 
