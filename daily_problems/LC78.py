#https://leetcode.cn/problems/subsets/description/

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subsets = [[]]
        for num in nums:
            subsets_containing_num = []
            for subset in subsets:
                subsets_containing_num.append([num] + subset)
            subsets.extend(subsets_containing_num)
            
        return subsets
