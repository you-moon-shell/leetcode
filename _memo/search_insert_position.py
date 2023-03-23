class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        low, high = 0, len(nums)-1
        while low <= high:
            print(low, high)
            print(nums[low:high+1])
            pivot = (low+high)//2
            if (nums[pivot] == target):
                return pivot
            elif (nums[pivot] < target):
                low = pivot+1
            else:
                high = pivot-1
            print(low, high)
        return low


_t = 7
_l1 = [1, 2, 3, 4, 5, 6, 8, 9]  # 6
_l2 = [1, 2, 3, 4, 5, 6, 8]  # 6

sl = Solution()
sl.searchInsert(_l1, _t)
sl.searchInsert(_l2, _t)
