#https://leetcode.cn/problems/maximum-unique-subarray-sum-after-deletion/description/

class Solution:
    def maxSum(self, nums: List[int]) -> int:
        dp = set()
        nums_neg = []
        max_sum = 0
        for num in nums:
            if num < 0:
                nums_neg.append(num)
                continue

            if num not in dp:
                max_sum += num
                dp.add(num)

        if 0 not in dp and max_sum == 0:
            max_sum = sorted(nums_neg)[-1]

        return max_sum