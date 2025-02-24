#https://leetcode.cn/problems/container-with-most-water/

class Solution:
    def maxArea(self, height: List[int]) -> int:
        i, j = 0, len(height) - 1
        max_v = 0

        while i < j:
            if height[i] <= height[j]:
                max_v = max(height[i] * (j - i), max_v)
                i += 1
            else:
                max_v = max(height[j] * (j - i), max_v)
                j -= 1

        return max_v
