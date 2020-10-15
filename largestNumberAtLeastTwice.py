class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        if len(nums)==0:
            return -1
        max_1=-1
        max_2=-1
        for i in range(0,len(nums)):
            if nums[i]>=max_1:
                max_2=max_1
                max_1=nums[i]
                index=i
            elif nums[i]>max_2:
                max_2=nums[i]
                
        if max_1<max_2*2:
            index=-1
        return index
