class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
    
        ans=[]
        count=0
        for i in range (len(nums)):
            for j in range(len(nums)) :
                if nums[j]<nums[i]:
                    count+=1
                     
            ans.append(count)
            count = 0
        return ans
