class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        sorted_nums=sorted(nums)
        array=[]
        n=len(nums)
        for i in range (n):
            if sorted_nums[i]==target:
                array.append(i)
        return array

