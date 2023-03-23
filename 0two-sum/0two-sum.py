class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        tbl={}
        for i,n in enumerate(nums):
            if n in tbl:
                return [tbl[n],i]
            tbl[target-n]=i
