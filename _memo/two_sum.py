class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        # ValueをKey、IndexをValueとして保持
        numToIndex = {}
        for i in range(len(nums)):
            # targetからnumberを引いた結果がdictに存在しているか確認
            if target - nums[i] in numToIndex:
                # あれば要件を満たすのでreturn
                return [numToIndex[target - nums[i]], i]
            # なければdictに追加
            numToIndex[nums[i]] = i
        return []


nums = [10, 20, 30, 40, 50, 6, 7, 8, 9, 10]
target = 56

print(Solution().twoSum(nums, target))
