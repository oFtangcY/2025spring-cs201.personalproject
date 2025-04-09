#https://leetcode.cn/problems/palindrome-partitioning/description/

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        output = []
        def divide(sub_str, out_str):
            if sub_str == '':
                output.append(out_str)
                return

            for i in range(1, len(sub_str) + 1):
                if sub_str[:i] == sub_str[:i][::-1]:
                    divide(sub_str[i:], out_str + [sub_str[:i]])

        divide(s, [])
        return output