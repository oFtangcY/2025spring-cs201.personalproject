class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 1:
            return [[1]]

        yanghui_tri = [[1], [1, 1]]
        row = 2
        while row < numRows:
            curr = [1]
            for i in range(row - 1):
                curr.append(yanghui_tri[row - 1][i] + yanghui_tri[row - 1][i + 1])
            curr.append(1)

            yanghui_tri.append(curr)
            row += 1

        return yanghui_tri
