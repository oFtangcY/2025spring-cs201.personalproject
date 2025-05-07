# https://leetcode.cn/problems/count-subarrays-where-max-element-appears-at-least-k-times/description/

class Solution:
    def countSubarrays(self, nums: list[int], k: int) -> int:
        n = len(nums)
        maxn = max(nums)
        left, right = 0, 0
        cnt = 0
        ans = 0
        while right < n:
            if nums[right] == maxn:
                cnt += 1

            if cnt >= k:
                while cnt >= k and left <= right:
                    if nums[left] == maxn:
                        cnt -= 1
                    left += 1
                cnt += 1
                left -= 1

                ans += left + 1

            right += 1

        return ans