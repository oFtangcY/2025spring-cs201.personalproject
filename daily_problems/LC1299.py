class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        right_max = -1
        n = len(arr)
        
        for i in range(n - 1, -1, -1):
            element = arr[i]
            arr[i] = right_max
            if element > right_max:
                right_max = element

        return arr
