#https://leetcode.cn/problems/h-index/description/

class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort(key=lambda x:-x)
        n = len(citations)

        if citations[-1] >= n:
            return n

        left, right = 0, n - 1
        while left < right:
            mid = (left + right) // 2
            if citations[mid] < mid + 1:
                right = mid
            else:
                left = mid + 1

        return left