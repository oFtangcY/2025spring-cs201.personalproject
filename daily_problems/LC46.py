#https://leetcode.cn/problems/permutations/description/

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        output = []

        def dfs(seq, in_nums):
            n = len(in_nums)
            if n == 0:
                output.append(seq)

            for i in range(n):
                if i == 0:
                    dfs(seq + [in_nums[i]], in_nums[1:])
                elif i == n - 1:
                    dfs(seq + [in_nums[i]], in_nums[:-1])
                else:
                    dfs(seq + [in_nums[i]], in_nums[:i] + in_nums[i + 1:])

        dfs([], nums)
        return output